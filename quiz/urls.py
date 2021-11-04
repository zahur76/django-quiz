from django.urls import path
from . import views

urlpatterns = [  
    path('', views.quiz, name='quiz'),
    path('add_quiz/', views.add_quiz, name='add_quiz'),
]
