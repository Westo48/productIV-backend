from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('notes.urls')),
    path('', include('todos.urls')),
    path('', include('users.urls')),
]
