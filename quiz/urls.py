from django.urls import path
from . import views

urlpatterns = [  
    path('', views.quiz, name='quiz'),
    path('add_quiz/', views.add_quiz, name='add_quiz'),
    path('delete_quiz/<int:quiz_id>', views.delete_quiz, name='delete_quiz'),
    path('update_quiz/<int:quiz_id>', views.update_quiz, name='update_quiz'),
    path('questionnaire/<int:quiz_id>', views.questionnaire, name='questionnaire'),
    path('add_question/<int:quiz_id>', views.add_question, name='add_question'),
]
