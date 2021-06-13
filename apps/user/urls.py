from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from apps.user import views

urlpatterns = [
    path('users/', views.UserAPI.as_view()),
    path('users/<int:pk>', views.UserAPIDetail.as_view()),

]
