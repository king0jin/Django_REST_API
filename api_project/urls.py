"""
URL configuration for api_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

#app애플리케이션에 있는 views.py내용 가져오기
from app import views

urlpatterns = [
    #admin요청이 왔을 때, admin.site에 있는 urls함수 호출
    path('admin/', admin.site.urls),
    #1. 기본 요청 설정
    path('', views.helloAPI), #app.views에 있는 helloAPI함수 호출
]
