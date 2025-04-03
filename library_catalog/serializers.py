from datetime import timezone
from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Book, Author, CustomUser, Transaction
from rest_framework.authtoken.models import Token


User = get_user_model()

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name']

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'isbn', 'published_date', 'number_of_copies']


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'date_of_membership', 'active_status']

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255)
    password = serializers.CharField(write_only=True)


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['id', 'book', 'user', 'check_out', 'returns']

class CheckOutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['book']

    def validate(self, data):
        user = self.context['request'].user
        book = data['book']

        
        if Transaction.objects.filter(user=user, book=book, returns__isnull=True).exists():
            raise serializers.ValidationError("You have already checked out this book.")

        
        if book.number_of_copies < 1:
            raise serializers.ValidationError("No available copies of this book.")

        return data

    def create(self, validated_data):
        book = validated_data['book']
        book.number_of_copies -= 1 
        book.save()
        return Transaction.objects.create(**validated_data, user=self.context['request'].user)

class ReturnSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['id']

    def validate(self, data):
        user = self.context['request'].user
        transaction = Transaction.objects.filter(user=user, id=data['id'], returns__isnull=True).first()

        if not transaction:
            raise serializers.ValidationError("No active checkout found for this transaction.")

        return data

    def update(self, instance, validated_data):
        instance.returns = timezone.now()
        instance.book.number_of_copies += 1 
        instance.book.save()
        instance.save()
        return instance