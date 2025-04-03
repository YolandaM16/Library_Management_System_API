from django.urls import path
from .views import RegisterView, LoginView, ReturnBookView, UserProfileView, AuthorList, AuthorDetail, BookList, BookDetail, CheckOutBookView, UserTransactionsView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='user-profile'),
    path('authors/', AuthorList.as_view(), name='authors'),
    path('authors/<int:pk>/', AuthorDetail.as_view(), name='authors-detail'),
    path('books/', BookList.as_view(), name='books'),
    path('books/<int:pk>/', BookDetail.as_view(), name='books-detail'),
    path('checkout/', CheckOutBookView.as_view(), name='checkout'),
    path('return/', ReturnBookView.as_view(), name='return-book'),
    path('transactions/', UserTransactionsView.as_view(), name='user-transactions'),
]