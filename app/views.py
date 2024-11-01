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

@api_view(['GET', 'POST'])
def booksAPI(request):
    if request.method == 'GET':
        #테이블의 전체 테이블 가져오기
        books = Book.objects.all()
        #가져온 데이터를 JSON문자열로 변환
        serializer = BookSerializer(books, many=True)
        #JSON으로 출력
        return Response(serializer.data, status.HTTP_200_OK)
    elif request.method == 'POST':
        #클라이언트가 입력한 데이터를 모델로 변환
        client_data = BookSerializer(data = request.data)
        #유효성 검사
        if client_data.is_valid():
            client_data.save() #유효성 검사를 통과라면 데이터베이스에 반영 
            return Response(client_data.data, status=status.HTTP_201_CREATED)
        return Response(client_data.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def bookAPI(request, book_id):
    #book_id에 해당하는 데이터 가져오기
    book = get_object_or_404(Book, book_id = book_id)
    #가져온 데이터를 JSON문자열로 변환
    serializer = BookSerializer(book)
    #JSON으로 출력
    return Response(serializer.data, status.HTTP_200_OK)