from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from clients.forms import UserForm, CategoryLogForm
from pymongo import MongoClient

from django.views.decorators.csrf import csrf_exempt

import os, json
from pathlib import Path



class MyMongoClient():
    def __init__(self):
        BASE_DIR = Path(__file__).resolve().parent.parent

        secret_file = os.path.join(BASE_DIR, 'secrets.json')

        with open(secret_file) as f:
            secrets = json.loads(f.read())

        self.client = MongoClient("mongodb+srv://mycl:{}@lecture.ks2gr.mongodb.net/myFirstDatabase?retryWrites=true&w=majority".format(secrets['MONGO_PW']))
        self.database = self.client["lecture"]

def main(request):
    if request.method == "POST":
        form  = CategoryLogForm(request.POST)
        
        if form.is_valid():
            form.save(commit=False)

        return render(request, 'clients/recommendationpage.html')
    return render(request, 'clients/landingpage.html')

def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        print(form)
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
    client = MyMongoClient()
    user_db = client.database["auth_user"]

    user = user_db.find_one({"id": user_id})
    return render(request, 'clients/mystoragepage.html', {'user': user})
    
def recommendation(request):
    return render(request, 'clients/recommendationpage.html')


@csrf_exempt
def review(request):
    client = MyMongoClient()
    ebsi = client.database["data_ebsi"]
    mega = client.database["data_megastudy"]
    etoos = client.database["data_etoos"]


    site_text = request.POST.get('site')

    search_key = request.POST.get('search_key')

    post_list = {}


    if(site_text=="ebsi") :
        if search_key :
            post_list = ebsi.find({"$or" : [{'title':{'$regex':search_key}} , {'title':search_key}]})
            print(post_list)
            return render(request, 'clients/reviewpage.html', {'post_list' : post_list})

    
    
    return render(request, 'clients/reviewpage.html', {'post_list' : post_list})





def for_review(request):
    return render(request, 'clients/for_reviewpage.html')

