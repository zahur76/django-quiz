from django.urls import path
from . import views

urlpatterns = [  
    path('', views.staff, name='staff'),
    path('add_staff', views.add_staff, name='add_staff'),
    path('delete_staff/<int:staff_id>', views.delete_staff, name='delete_staff'),
    path('quiz_results', views.quiz_results, name='quiz_results'),
    path('delete_result/<int:result_id>', views.delete_result, name='delete_result'),
]
