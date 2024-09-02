"""
URLs for messenger/
"""
from django.urls import path

from messenger import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dialogues/', views.dialogues, name='dialogues'),
]