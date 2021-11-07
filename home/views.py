from django.db.models.query_utils import Q
from django.shortcuts import get_object_or_404, render
from django.contrib import messages
from quiz.models import Quiz
from staff.models import Staff
from quiz.views import random_number_encode

# Create your views here.
def home(request):
    """ A view to return the home page """
    if request.method == 'POST':
        employee_num = int(request.POST['employee_num'])
        try:
            staff = Staff.objects.get(employee_number=employee_num)
        except Staff.DoesNotExist:
            messages.error(
            request, 'Incorrect Employee Number!')
            return render(request, 'home/index.html')
        quizzes = Quiz.objects.all()
        encode_quiz= []
        tempo_dict = {}
        if staff:
            request.session['employee']= {'employee': staff.employee_number}
            for quiz in quizzes:
                tempo_dict['id']=(random_number_encode(quiz.id, 1))
                tempo_dict['quiz_name'] = quiz.quiz_name
                encode_quiz.append(tempo_dict)
                tempo_dict = {}
            context = {
                'quizzes': encode_quiz,
                'staff': staff,
            }
            return render(request, 'home/index.html', context)

    return render(request, 'home/index.html')
