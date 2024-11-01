from django.urls import path
from .views import helloAPI, booksAPI

urlpatterns = [
    #1. hello/요청이 왔을 때, helloAPI함수 호출
    path("hello/", helloAPI),
    #3. books/요청이 왔을 때, booksAPI함수 호출
    path("books/", booksAPI), #CRUD - 전체 데이터 조회
]