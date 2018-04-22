from django.urls import path
from FirstApp import views

urlpatterns = [
    path('',views.users, name = 'users')
]
