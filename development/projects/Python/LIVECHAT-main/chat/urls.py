from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('logIn/', views.loginpage, name = 'login'),
    path('signUp/', views.register, name = 'register'),
    path('inbox/', views.inbox, name = 'inbox')
]