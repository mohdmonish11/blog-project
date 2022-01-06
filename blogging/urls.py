"""blogging URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.homepage),
    path('homepage/', views.homepage),
    path('login/', views.login),
    path('check_login_details',views.check_login_details),
    path('signup/', views.sign_up),
    path('sign_up', views.sign_up_data_fetch),
    path('S_login/', views.s_login),
    path('createPost/', views.createPost),
    path('editPost/', views.editPost),
    path('editPost_update',views.editPost_update),
    path('deletePost/', views.deletePost),
    path('delete_post',views.delete_post),
    path('viewPost/', views.viewPost),
    path('searchPost/', views.searchPost),
    path('search_Post',views.searchPostresult),
    path('forgetpass/', views.forgetpass),
    path('update_password',views.update_password),
    path('insert_article',views.insert_article),

]
