from django.contrib import admin
from django.urls import path, include

from . import views


urlpatterns = [
    path('', views.DepartmentView.as_view()),
    path('department/<int:id>/', views.DepartmentView.as_view()),
]
