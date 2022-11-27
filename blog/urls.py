from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('postComment', views.postComment, name="postComment"),
    path('', views.blogHome, name="bloghome"),
    path('coepblog', views.coepblogHome, name="coepbloghome"),
    path('allblog', views.allblog, name="allblog"),
    path('<str:slug>', views.blogPost, name="blogPost"),
]
