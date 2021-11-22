from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('user/storage/', views.user_storage, name='storage'),
    
    path('recommendation/', views.recommendation, name='recommendation'),
    path('review/', views.review, name='review'),
]