from django.shortcuts import (
    render, redirect, reverse, get_object_or_404)
from django.contrib import messages
from .forms import add_quizForm, add_questionForm
from .models import Quiz, Questions

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
    questions = Questions.objects.all().filter(quiz=quiz_id)
    if quiz:
        quiz.delete()
    if questions:
        questions.delete()    
    messages.success(request, 'Quiz record deleted!')
    return redirect(reverse('quiz'))

def update_quiz(request, quiz_id):
    """View to update quiz name"""
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

def questionnaire(request, quiz_id, num=0):
    """View to view Questionnaire"""
    print(num)
    quiz = get_object_or_404(Quiz, id=quiz_id)
    questions = Questions.objects.all().filter(quiz=quiz_id)
    question_id=[]
    for question in questions:
        question_id.append(question.id)
    print(question_id)
    actual_question = get_object_or_404(Questions, id=question_id[num])
    
    final = len(question_id)
    print(final)
    print(num)
    context = {
        'final': final,
        'next': num+1,
        'quiz': quiz,
        'question': actual_question,
    }
    return render(request, 'quiz/questionnaire.html', context)

def add_question(request, quiz_id):
    """View to add Questions"""
    if not request.user.is_superuser:
        messages.error(request, 'Permision Denied!.')
        return redirect(reverse('home'))
    quiz = get_object_or_404(Quiz, id=quiz_id)
    if request.method == 'POST':
        form = add_questionForm(request.POST)        
        if form.is_valid():
            question_form = form.save(commit=False)
            question_form.quiz=quiz
            question_form.save()
            messages.success(request, 'Question Added!')
            return redirect(reverse('quiz'))
        messages.error(
            request, 'Question could not be added, try again!')

    form = add_questionForm()
    context = {
        'quiz': quiz,
        'form': form,
    }
    return render(request, 'quiz/add_question.html', context)