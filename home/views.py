from django.db.models.query_utils import Q
from django.shortcuts import get_object_or_404, render
from django.contrib import messages
from quiz.models import Quiz
from staff.models import Staff

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
        if staff:
            context = {
                'quizzes': quizzes,
                'staff': staff,
            }
            return render(request, 'home/index.html', context)

    return render(request, 'home/index.html')
