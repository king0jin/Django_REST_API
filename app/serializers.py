#모델의 데이터를 JSON으로 변환해서 출력하기위한 Serializer생성
from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['book_id', 'book_name', 'author', 'category', 'price', 'published_date']