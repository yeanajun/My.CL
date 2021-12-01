from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from clients.forms import UserForm
from pymongo import MongoClient

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
    return render(request, 'clients/landingpage.html')

def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        print(form)
        if form.is_valid():
            print("success")
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)  # 사용자 인증
            login(request, user)  # 로그인
            return redirect('main')
    else:
        form = UserForm()
    return render(request, 'clients/registerpage.html', {'form': form})

def user_storage(request):
    return render(request, 'clients/mystoragepage.html')
    
def recommendation(request):
    return render(request, 'clients/recommendationpage.html')

def review(request):
    client = MyMongoClient()
    ebsi = client.database["data_ebsi"]
    mega = client.database["data_megastudy"]
    etoos = client.database["data_etoos"]

    list_ebsi = ebsi.find()
    list_mega = mega.find()
    list_etoos = etoos.find()

    return render(request, 'clients/reviewpage.html', {"list_ebsi": list_ebsi, "list_mega" : list_mega , 'list_etoos':list_etoos})

def for_review(request):
    return render(request, 'clients/for_reviewpage.html')

