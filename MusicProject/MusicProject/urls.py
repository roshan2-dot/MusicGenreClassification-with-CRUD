"""MusicProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django import views
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from MusicApp.views import file_upload_view
from MusicApp.views import Edit
from MusicApp.views import Update
from MusicApp.views import Delete
from MusicApp.views import model_form_upload




urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('MusicApp.urls')),
    path('upload/',file_upload_view,name='upload-view'),
    path('edit/', Edit, name='edit'),
    path('update/<audio_id>', Update, name='update'),
    path('delete/<audio_id>', Delete, name='delete'),
    path('result/', model_form_upload, name='result'),
]   

handler404 = 'MusicApp.views.handle_not_found'