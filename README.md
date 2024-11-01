# Django_REST_API
Django로 REST API 만들기


**pip install django**


**pip install djangorestframework**


**pip install mysqlclient**

## Djangoframework : Django와 다른 점
1. API 응답에서 HTTP 헤더에 대한 더 많은 세부정보를 설정하고 처리할 수 있다.
2. JSON과 같은 데이터 포맷으로 응답을 제공하여 클라이언트가 데이터를 쉽게 처리할 수 있도록 한다.
3. Serializer를 사용하여 복잡한 데이터 타입을 JSON, XML 등 다양한 포맷으로 변환할 수 있다

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

## 프로젝트의 역할
1. 프로젝트는 하나 이상의 웹 애플리케이션을 포함할 수 있다
2. 프로젝트 urls.py : 프로젝트 전체의 URL라우팅을 조정하는 역할을 한다
## 애플리케이션의 역할
1. 프로젝트를 구성하는 각 기능이 고유한 URL공간을 갖고 충돌을 방지한다
2. 애플리케이션 views.py : 요청 URL의 처리 함수를 정의한다
### 애플리케이션에 urls.py를 생성하는 이유
+ 프로젝트 하나의 urls.py에 URL을 정의하면 관리하기 어려움으로 애플리케이션 별로 urls.py를 생성하여 해당 애플리케이션 관련 URL을 관리, 수정 할 수 있다.


**프로젝트 urls.py에 include를 사용하여 각각의 애플리케이션 URL설정을 하여 인식할 수 있게 하면된다**

## Response
요청에 대한 응답 결과를 만들기 위한 클래스이다

응답 결과를 알려줄 때는 상태코드를 같이 전송해서 정상 처리여부를 알려주는 것이 좋다
+ status : 상태코드

## serializers.py
모델의 데이터를 JSON문자열로 변환해서 출력해준다

## Django REST Framework에서 제공하는 데코레이터 : @api_view
1. 허용할 HTTP메서드 목록을 지정할 수 있다
2. 요청 데이터에 대한 유효성 검사, 오류 처리 로직을 간단하게 작성할 수 있다 - 요청 데이터에 따른 서로 다른 로직 구
3. HTTP응답을 쉽게 반환할 수 있도록 해준다 - Response 객체를 사용하여 JSON형태로 응답을 반환
4. 기본 적인 권한, 인증 처리와 함께 사용할 수 있다



  

