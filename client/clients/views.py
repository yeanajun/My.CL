from django.shortcuts import render, redirect

def main(request):
    return render(request, 'clients/landingpage.html')

def login(request):
    return render(request, 'clients/loginpage.html')

def logout(request):
    return redirect('main')

def signup(request):
    return render(request, 'clients/registerpage.html')

def user_storage(request):
    return render(request, 'clients/mystoragepage.html')
    
def recommendation(request):
    return render(request, 'clients/recommendationpage.html')

def review(request):
    return render(request, 'clients/reviewpage.html')