# My.CL

## 프로젝트 설명
이 프로젝트는 인터넷 강의 추천 시스템으로, 학생들 각각의 취향을 반영하여 인터넷 강의를 추천해주어 강의를 찾는 시간을 줄여주는 웹서비스입니다.

<img id="logo" alt="My.Cl 로고" width = "30%" src="/client/clients/static/img/로고.jpg" />

## 구동 방법
프로젝트 구현 폴더는 client로, 먼저 client 폴더를 실행하고
```
cd client
```
가상환경을 실행시켜줍니다.
```
python -m venv ./venv
cd venv
source Scripts/activate
```
필요 라이브러리를 client/requirements.txt에서 설치할 수 있습니다.
```
cd ..
pip install -r requirements.txt
```
비로소 Django 서버를 실행시킬 수 있습니다.
```
python manage.py runserver
```

## 의존성 Dependencies

python==3.9.2

asgiref==3.4.1<br/>
dj-database-url==0.5.0<br/>
Django==3.1.12<br/>
django-dotenv==1.4.2<br/>
django-heroku==0.3.1<br/>
djongo==1.3.6<br/>
dnspython==2.1.0<br/>
gunicorn==20.1.0<br/>
psycopg2==2.9.2<br/>
pymongo==3.12.1<br/>
python-snappy==0.6.0<br/>
pytz==2021.3<br/>
sqlparse==0.2.4<br/>
whitenoise==5.3.0<br/>
winkerberos==0.8.0
<br/>
## 이외 폴더 설명
* crawling_code
<br/>각 강의 사이트별 강의 목록을 크롤링할 때 사용한 코드가 포함되어 있습니다.

* data
<br/>강의 목록 데이터 및 각 강의 태그 랜덤값을 생성한 코드가 포함되어 있습니다.
  
* previous_json_structure
<br/>데이터베이스 구조 beta 코드 내용 및 샘플 구조가 포함되어 있습니다.      

* rec_algorithm
<br/>후기 작성 시 카테고리 count 증가 및 추천 알고리즘 파이썬 코드가 포함되어 있습니다. 
