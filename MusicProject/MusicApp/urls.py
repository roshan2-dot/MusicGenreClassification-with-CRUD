from django.contrib import admin
from django.urls import path
from MusicApp import views;

urlpatterns = [
    path('', views.index, name = 'home'),
    path('classify', views.classify, name = 'classify'),
    path('category',views.category,name = 'category'),
    path('about',views.about, name = 'about'),
    path('result',views.result, name = 'result'),
]