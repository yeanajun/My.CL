from django.http import request
from django.shortcuts import render, redirect
from django.contrib import messages 
from django.contrib.auth import authenticate, login
from clients.forms import ReviewForm
from clients.models import CategoryLog,ReviewLog
from clients.forms import UserForm, CategoryLogForm, ReviewForm
from pymongo import MongoClient

from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator

import os, json
from bson.objectid import ObjectId
from pathlib import Path

#mongoDB서버 연동
def connect_lecture_db():
    BASE_DIR = Path(__file__).resolve().parent.parent

    secret_file = os.path.join(BASE_DIR, 'secrets.json')
    with open(secret_file) as f:
        secrets = json.loads(f.read())
    mongodb_uri = "mongodb+srv://mycl:{}@lecture.ks2gr.mongodb.net/mycl?retryWrites=true&w=majority".format(os.environ.get('MONGO_PW'))
    myclient = MongoClient(mongodb_uri)
    mydb = myclient.get_database("lecture")
    return mydb

#_id값 찾기 -> connect_lecture_db()와 연결 되어있음
#title 제목으로 searching 시 _id값 하나 반환
def searching_id(key_name, value_name, site_name):
    lecture_id_list = []
    mycol = connect_lecture_db().get_collection(site_name)
    for di in mycol.find({}, {key_name: 1}):
        if di.get(key_name) == value_name:
            if key_name == "title":
                lecture_id = di.get("_id")
                return lecture_id
            else:
                lecture_id_list.append(di.get("_id"))

    return lecture_id_list


#과목, 학년으로 뽑아낸 list 교집합 ->lecture_id_list
#list2개 교집합 list형태로 반환
def list_intersection(list1, list2):
    li = list(set(list1).intersection(list2))
    return li

#_id와 tag_data값으로 dict만들기
def data_make_dict(lecture_id_list, tag_name, tag_data):
    id_list = []
    tag_value = []
    mycol = connect_lecture_db().get_collection(tag_name)
    for di in mycol.find({}, {tag_data: 1}):
        for i in range(len(lecture_id_list)):
            if di.get("_id") == lecture_id_list[i]:
                id_list.append(di.get("_id"))
                tag_value.append(di.get(tag_data))
    dic = dict(zip(id_list, tag_value))
    return dic

#dict에서 특정한 수의 max값 추출 하여 list로 반환
def max_filtering(dic_length, dic):
    max_id_data = []
    cnt = 0
    while(cnt < dic_length*9/10):
        if dic_length <= 5:
            return list(dic.keys())                     #5개 이하면 그대로 key값만 반환
        else:
            max_data = max(dic, key=dic.get)
            max_id_data.append(max_data)
            del dic[max_data]
            cnt += 1

    return max_id_data

#리뷰데이터 코멘트 로딩
def review_comment_load(idv):
    key = ReviewLog.objects.all()
    for k in key:
        if key.lecture_id == idv:
            return key.lec_comment
        else:
            pass

#결과값 title을 list로 반환
def recommendation_res_title(res_list, tag_name):
    rec_res_list = []
    mycol = connect_lecture_db().get_collection(tag_name)

    for i in res_list:
        for di in mycol.find():
            if di.get("_id") == i:
                di.pop("_id")
                temp = list(di.values())
                # temp.append(review_comment_load(i))         #comment부분 추가
                rec_res_list.append(temp)
    return rec_res_list

#tag 값 update
def update_tag_data(lecture_id, tag_name, tag_data):
    
    mycol = connect_lecture_db().get_collection(tag_name)
    for di in mycol.find({}, {tag_data: 1}):
        temp = di.get(tag_data) + 1

        if di.get("_id") == ObjectId(lecture_id):  # lecture에서 찾은 id값과 tag_ ***의 id값 일치 --> 태그값 +1 후에 수정
            mycol.update_one({"_id": ObjectId(lecture_id)}, {"$set": {tag_data: temp}})

            

#가장 최신 리뷰 데이터 update
def reviewlog_load():
    key = ReviewLog.objects.last()
    update_tag_data(key.lecture_id, "tag_achivement", key.achivement)
    update_tag_data(key.lecture_id, "tag_jobdam", key.tag_jobdam)
    update_tag_data(key.lecture_id, "tag_pilgi", key.tag_pilgi)
    update_tag_data(key.lecture_id, "tag_jindo", key.tag_jindo)

#사용자가 선택한 tag_data 딕셔너리
def choice_tag_dict(key):
    tag_dict = {"jobdam": key.tag_jobdam,
                "jindo": key.tag_jindo,
                "pilgi": key.tag_pilgi,
                "site": key.site,
                "achivement": key.achivement
                }
    return tag_dict
################################################################################

def main(request):
    if request.method == "POST":
        form  = CategoryLogForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)  
            form.user_id = request.user.id
            form.save()
            return redirect('recommendation')
        
        else:
            messages.error(request, "모든 카테고리를 선택해주세요.")
    return render(request, 'clients/landingpage.html')

@csrf_exempt
def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)  # 사용자 인증
            login(request, user)  # 로그인
            return redirect('main')
    else:
        form = UserForm()
    return render(request, 'clients/registerpage.html', {'form': form})

def user_storage(request, user_id):
    user_db = connect_lecture_db().get_collection("auth_user")
    category_log = connect_lecture_db().get_collection("clients_categorylog")
    review_log = connect_lecture_db().get_collection("clients_reviewlog")

    user = user_db.find_one({"id": user_id})
    category = category_log.find({"user_id": user_id})
    review = review_log.find({"user_id": user_id})

    return render(request, 'clients/mystoragepage.html', {'user': user, 'category': category, 'review': review})
    
def recommendation(request):
    key = CategoryLog.objects.last()

    #문자열 부분 사이트에서 데이터 받아와야 함
    lecture_id_list1 = searching_id("subject", key.subject, "data_{}".format(key.site))
    lecture_id_list2 = searching_id("grade", key.grade, "data_{}".format(key.site))
    intersection_id_list = list_intersection(lecture_id_list1, lecture_id_list2)

    dic = data_make_dict(intersection_id_list, "tag_jindo", key.tag_jindo)
    dic2 = data_make_dict(max_filtering(len(dic),dic), "tag_jobdam", key.tag_jobdam)
    dic3 = data_make_dict(max_filtering(len(dic2),dic2), "tag_pilgi", key.tag_pilgi)
    dic4 = data_make_dict(max_filtering(len(dic3),dic3), "tag_achivement", key.achivement)

    reslist = max_filtering(len(dic4), dic4)
    rec_res_list = recommendation_res_title(reslist, "data_{}".format(key.site))
    cho_tag = choice_tag_dict(key)

    # x 눌렀을 시 2개씩 계속 출력
    paginator = Paginator(rec_res_list, 2)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    # recommendation log 추가
    rec_log_db = connect_lecture_db().get_collection("clients_recommendationlog")
    log = {'user_id': key.user_id, 'lec_list': rec_res_list}
    rec_log_db.insert(log)

    return render(request, 'clients/recommendationpage.html', {"list": rec_res_list, 'posts': posts, 'cho_tag' : cho_tag})


@csrf_exempt
def review(request):
    ebsi = connect_lecture_db().get_collection("data_ebsi")
    mega = connect_lecture_db().get_collection("data_megastudy")
    etoos = connect_lecture_db().get_collection("data_etoos")
    site_text = request.POST.get('site')
    search_key = request.POST.get('search_key')
    post_lec = {}
    if(site_text=="ebsi") :
        if search_key :
            post_lec = ebsi.find({"$or" : [{'title':{'$regex':search_key}} , {'title':search_key}]})
            return render(request, 'clients/reviewpage.html', {'post_lec' : post_lec})
    elif(site_text=="mega") :
        if search_key :
            post_lec = mega.find({"$or" : [{'title':{'$regex':search_key}} , {'title':search_key}]})
            return render(request, 'clients/reviewpage.html', {'post_lec' : post_lec})
    elif(site_text=="etoos") :
        if search_key :
            post_lec = etoos.find({"$or" : [{'title':{'$regex':search_key}} , {'title':search_key}]})
            return render(request, 'clients/reviewpage.html', {'post_lec' : post_lec})            
    
    return render(request, 'clients/reviewpage.html', {'post_lec' : post_lec})


@csrf_exempt
def for_review(request):
    ebsi = connect_lecture_db().get_collection("data_ebsi")
    mega = connect_lecture_db().get_collection("data_megastudy")
    etoos = connect_lecture_db().get_collection("data_etoos")

    lecture_title = request.GET.get('lecture_select')

    EBS = ebsi.find()
    MEGA = mega.find()
    ETO = etoos.find()

    lecture = {}

    for lec in EBS :
        if(lec.get("title") == lecture_title):
            lecture = lec
    for lec in MEGA :
        if(lec.get("title") == lecture_title):
            lecture = lec
    for lec in ETO :
        if(lec.get("title") == lecture_title):
            lecture = lec



    return render(request, 'clients/for_reviewpage.html', {'lecture' : lecture})


def get_review(request, lecture_title):
    
    if request.method == "POST":
        review_form  = ReviewForm(request.POST)
        if review_form.is_valid():
            review_form = review_form.save(commit=False)  
            review_form.user_id = request.user.id
            

            review_form.lecture_title = lecture_title
            for site in ['ebsi', 'megastudy', 'etoos']:
                if searching_id("title", lecture_title, "data_{}".format(site)):
                    review_form.lecture_id = searching_id("title", lecture_title, "data_{}".format(site))
                    break

            review_form.save()
            messages.info(request, "후기 등록이 완료되었습니다.")
            reviewlog_load()
            return redirect('main')
        
        else:
            messages.error(request, "모든 카테고리를 선택해주세요.")


    return render(request, 'clients/for_reviewpage.html')
