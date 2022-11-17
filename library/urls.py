from django.urls import path 
from .views import BookDetailView, BooksView

urlpatterns = [
    path('', BooksView.as_view(), name='books'),
    path('<int:pk>/', BookDetailView.as_view(), name='book')
]