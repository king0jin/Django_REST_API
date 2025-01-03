from django.urls import path
from .views import helloAPI, booksAPI, bookAPI
#ajax요청 추가
from .views import ajax, axios

urlpatterns = [
    #1. hello/요청이 왔을 때, helloAPI 호출
    path("hello/", helloAPI),
    #3. books/요청이 왔을 때, booksAPI 호출
    path("books/", booksAPI), #CRUD - 전체 데이터 조회, 데이터 삽입
    #4. book/book_id 요청이 왔을 때, bookAPI 호출
    path("book/<int:book_id>", bookAPI), #CRUD - 특정 데이터 조회   
    #5. ajax요청이 왔을 때, ajax 호출 
    path('ajax/', ajax),
    #6. axios요청이 왔을 때, axios 호출
    path('axios/', axios)
]