from rest_framework import serializers

from .models.book import Book
from .models.author import Author

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Book

class BookReadSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    class Meta:
        fields = '__all__'
        model = Book

class AuthorSerializer(serializers.ModelSerializer):
    class Meta: 
        fields = '__all__'
        model = Author