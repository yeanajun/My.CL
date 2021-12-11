from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('login/', auth_views.LoginView.as_view(template_name='clients/loginpage.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('<int:user_id>/storage/', views.user_storage, name='storage'),
    
    path('recommendation/', views.recommendation, name='recommendation'),
    path('review/', views.review, name='review'),
    path('for_review/', views.for_review, name = 'for_review'),
    path('get_review/<str:lecture_title>', views.get_review, name = 'get_review'),
]