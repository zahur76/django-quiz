from django.shortcuts import (
    render, redirect, reverse, get_object_or_404)
from django.contrib import messages
from .forms import add_quizForm
from .models import Quiz

# Create your views here.
def quiz(request):
    """View for quiz management"""
    if not request.user.is_superuser:
        messages.error(request, 'Permision Denied!.')
        return redirect(reverse('home'))
    quizzes = Quiz.objects.all()
    context = {
        'quizzes': quizzes,
    }

    return render(request, 'quiz/quiz.html', context)

def add_quiz(request):
    """View to add quiz"""
    if not request.user.is_superuser:
        messages.error(request, 'Permision Denied!.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = add_quizForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Quiz Added!')
            return redirect(reverse('quiz'))

        messages.error(
            request, 'Quiz could not be added!')
        new_form = add_quizForm()
        context = {
            'form': new_form,
            }
        return render(request, 'staff/add_quiz.html', context)
    form = add_quizForm()
    context = {
        'form': form,
    }
    return render(request, 'quiz/add_quiz.html', context)

def delete_quiz(request, quiz_id):
    """View for quiz management"""
    if not request.user.is_superuser:
        messages.error(request, 'Permision Denied!.')
        return redirect(reverse('home'))
    quiz = get_object_or_404(Quiz, id=quiz_id)
    quiz.delete()
    messages.success(request, 'Quiz record deleted!')
    return redirect(reverse('quiz'))

def update_quiz(request, quiz_id):
    """View for quiz management"""
    if not request.user.is_superuser:
        messages.error(request, 'Permision Denied!.')
        return redirect(reverse('home'))
    quiz = get_object_or_404(Quiz, id=quiz_id)          
    if request.method == 'POST':        
        form = add_quizForm(request.POST, request.FILES, instance=quiz)
        if form.is_valid():
            form.save()
            messages.success(request, 'Quiz updated!')
            return redirect(reverse('quiz'))
        else:
            messages.error(
                request, 'Quiz could not be updated. \
                    Tru again.')
            return redirect(reverse('quiz'))
    form = add_quizForm(instance=quiz)
    context = {
        'form': form,
        'quiz': quiz,
        }
    return render(request, 'quiz/update_quiz.html', context)