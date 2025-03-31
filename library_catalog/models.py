from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    isbn = models.CharField(max_length=13, unique=True)
    published_date = models.DateField()
    number_of_copies = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.title} by {self.author.name}"
    

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    date_of_membership = models.DateField(auto_now_add=True)
    active_status = models.BooleanField(default=True)

    groups = models.ManyToManyField(Group, related_name='customuser_set', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='customuser_permissions_set', blank=True)

    def __str__(self):
        return self.username
    

class Transaction(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='Transactions')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE,related_name='Transactions')
    check_out = models.DateTimeField(auto_now_add=True)
    returns = models.DateTimeField()

    def __str__(self):
        return f"{self.user.username} borrowed {self.book.title}"