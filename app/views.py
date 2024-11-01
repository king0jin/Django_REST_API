#템플릿 엔진을 이용해서 HTML출력에 사용
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Book
from .serializers import BookSerializer

from rest_framework import status
from rest_framework.generics import get_object_or_404


@api_view(['GET'])
def helloAPI(request):
    return Response("hello!")

@api_view(['GET'])
def booksAPI(request):
    #테이블의 전체 테이블 가져오기
    books = Book.objects.all()
    #가져온 데이터를 JSON문자열로 변환
    serializer = BookSerializer(books, many=True)
    #JSON으로 출력
    return Response(serializer.data, status.HTTP_200_OK)

@api_view(['GET'])
def bookAPI(request, book_id):
    #book_id에 해당하는 데이터 가져오기
    book = get_object_or_404(Book, book_id = book_id)
    #가져온 데이터를 JSON문자열로 변환
    serializer = BookSerializer(book)
    #JSON으로 출력
    return Response(serializer.data, status.HTTP_200_OK)