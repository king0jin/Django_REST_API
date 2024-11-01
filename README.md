# Django_REST_API
Django로 REST API 만들기
**pip install django**
**pip install djangorestframework**
**pip install mysqlclient**

## 프로젝트와 애플리케이션 생성하기
### 프로젝트 생성
**django-admin startproject 프로젝트이름 경로**
+ 내가 설정한 프로젝트이름의 디렉토리와 manage.py가 생성된다.
### 애플리케이션 생성하기
**python manage.py startapp 애플리케이션이름**
+ 내가 설정한 애플리케이션이름의 디렉토리가 생성된다.

## 실행하기
**python manage.py runserver IP주소:포트번호**
+ 포트번호를 생략하면 **8000**번으로 자동 설정된다.
+ 로컬에서 실행하여 접속할 시 IP주소는 **127.0.0.1**이다 
  + Chrome브라우저에 **127.0.0.1:8000**으로 검색하면 django화면을 볼 수 있다.

## settings.py
### 프로젝트 설정 파일
secret key, debug mode, 개발환경에서 수행되는 내용을 다르게 만들고 할 때 등등의 설정을 할 수 있다
+ INSTALLED_APPS
  + 사용할 패키지와 애플리케이션 기재
    + rest_framework
    + 애플리케이션이름 
+ DATABASE
  + 기본으로 sqlite3로 설정되어 있다
  + mysql설정으로 변경하여 데이터베이스를 연동한다
+ TIME_ZONE
  + Asia/Seoul로 수정한다 
