from django.urls import path
from .views import RegisterView, LoginView, UserProfileView, AuthorList, AuthorDetail, BookList, BookDetail

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='user-profile'),
    path('authors/', AuthorList.as_view(), name='authors'),
    path('authors/<int:pk>/', AuthorDetail.as_view(), name='authors-detail'),
    path('books/', BookList.as_view(), name='books'),
    path('books/<int:pk>/', BookDetail.as_view(), name='books-detail')
]