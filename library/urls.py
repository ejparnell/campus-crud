from django.urls import path 
from .views.book_views import BooksView, BookDetailView
from .views.author_views import AuthorsView, AuthorDetailView

urlpatterns = [
    path('books/', BooksView.as_view(), name='books'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book'),
    path('authors/', AuthorsView.as_view(), name='authors'),
    path('authors/<int:pk>/', AuthorDetailView.as_view(), name='author'),
]