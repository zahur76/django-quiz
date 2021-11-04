from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import add_quizForm

# Create your views here.
def quiz(request):
    """View for quiz management"""
    if not request.user.is_superuser:
        messages.error(request, 'Permision Denied!.')
        return redirect(reverse('home'))

    return render(request, 'quiz/quiz.html')

def add_quiz(request):
    """View to add quiz"""
    if not request.user.is_superuser:
        messages.error(request, 'Permision Denied!.')
        return redirect(reverse('home'))
    
    form = add_quizForm()

    context = {
        'form': form,
    }
    return render(request, 'quiz/add_quiz.html', context)
    