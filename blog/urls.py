from django.contrib import admin
from django.urls import path, include
from blog import views

urlpatterns = [
    path('article/', views.ArticleView.as_view()),
]
