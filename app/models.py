from django.db import models

# Create your models here.
#도서 정보를 저장하기위한 모델 = 테이블
class Book(models.Model):
    book_id = models.IntegerField(primary_key=True)
    book_name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    price = models.IntegerField()
    published_date = models.DateField()