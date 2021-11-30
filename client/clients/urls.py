from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('login/', auth_views.LoginView.as_view(template_name='clients/loginpage.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('user/storage/', views.user_storage, name='storage'),
    
    path('recommendation/', views.recommendation, name='recommendation'),
    path('review/', views.review, name='review'),
    
]