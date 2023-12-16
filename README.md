# My.CL

<img id="logo" alt="My.Cl 로고" width = "30%" src="/client/clients/static/img/로고.jpg" />

### 🔳 요약

- **사용자 취향의 입력을 기반으로 학생들에게 적절한 강의를 추천**
    
    → 유저들은 후기 데이터를 통해 개인의 능력과 취향을 바탕으로 단순히 인기 있는 강사의 강의가 아닌 본인에게 맞는 강의를 추천 받을 수 있습니다.

### 🔳 프로젝트 개발 내용

- 사용자들의 학년, 등급, 수강하고 싶은 강의, 강의 사이트 등을 기본으로 입력을 받도록 구성했습니다.
- 추가적으로 잡담양, 필기양, 진도 등 다소 주관적일 수 있는 부분을 후기 데이터로 얻어 입력을 받게 되면 그에 맞는 강의를 추천하게 됩니다.

- 강의에 대한 정보가 표시되고 강의 사이트로 넘어 갈 수 있게 됩니다. 추천 알고리즘에 따라 추천 순위가 높은 것부터 다음 결과를 클릭하면 넘어가게 됩니다.

- 사용자는 수강한 강의에 대한 후기를 작성 할 수 있으며 이는 이후의 추천 결과에 반영되게 됩니다.

- 로그인 한 사용자에 한에서 이전 선택한 카테고리와 후기 데이터를 확인 할 수 있습니다.

### 🔳주요 업무

- **후기 데이터를 통한 DB load, update 알고리즘 구현**
- **DB의 후기 데이터를 통한 강의 추천 알고리즘 제작**
  
  
### 🔳 결과 및 회고

- Cold Start인 프로젝트의 문제로 임의로 집어넣은 데이터를 통한 추천으로 완성도가 다소 떨어졌고 ai모델을 사용하지 않고 단순 알고리즘 적인 추천 알고리즘을 제작 했다는 점이 아쉬움으로 남았습니다.

- Python 뿐만 아니라 JavaScript를 사용하고 Django 프레임워크를 사용해 보는 경험을 얻었고 처음으로 git을 사용한 프로젝트로 많은 것을 얻어갔습니다.

### 🔳 추가 작업

- 개발 당시 Recommendation system과 인공지능에 대한 지식이 부족하여 특정 feature들의 후기 데이터 수와 임의로 설정한 가중치에 따라 순서를 부과하여 추천하는 방식을 사용했습니다.

- **Collaborative Filtering의 Matrix Factorization을 응용하여 새로운 추천 시스템으로 발전시켜 보았습니다.**
    - 학생들이 강의를 선택한 것이 학생들(User)과 강의(Item)간의 Matrix로 구성되어 있다고 생각해보았습니다.
    - **Rating Matrix(R)** = **(User * K) X (K * Item) => User * Item**
        
        **(K를 잡담양, 필기양 등의 feature로 생각)**
        
    
    - 기본적인 Matrix Factorization 모델 구조에서 후기 데이터 DB에 존재하는 K를 기반으로 학습을 진행하여 평점 예측을 진행하고 높은 score의 강의부터 차례로 추천을 진행하는 방식으로 구현해 보았습니다.
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
