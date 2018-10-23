from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from states import views

urlpatterns = [
    path('', views.StateList.as_view()),   
]