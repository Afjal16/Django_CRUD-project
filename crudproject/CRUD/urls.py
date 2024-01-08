from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('delete/<id>', views.delete, name='delete'),
    path('edit/<id>', views.edit, name='edit'),
    path('update/<id>', views.update, name='update'),
    path('add_book/', views.add_book, name='add_book'),
    path('create/', views.create, name='create'),
    
]