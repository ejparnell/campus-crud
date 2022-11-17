from django.shortcuts import render, get_object_or_404
from library.serializers import BookSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Book

# Create your views here.
#localhost:3000/books/ get post
class BooksView(APIView):
    """View class for books/ for viewing all and creating"""
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response({'books': serializer.data})


#localhost:3000/books/:id get delete update
class BookDetailView(APIView):
    """View class for books/:pk for viewing a single book, updating a single book, or removing a single book"""