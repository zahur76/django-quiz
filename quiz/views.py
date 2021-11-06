import secrets
import string
import json
import math
from django.shortcuts import (
    render, redirect, reverse, get_object_or_404, HttpResponse)
from django.contrib import messages
from .forms import add_quizForm, add_questionForm
from .models import Quiz, Questions
from staff.models import Staff

def randon_word(length):
    """Generate random word"""
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(alphabet) for i in range(length))

    return password

def save_answer(request):
    """View to save answer to session"""
    request.session.modified = True
    result = request.POST.get('answer')
    answer_id = request.POST.get('id')

    if request.user.is_superuser:
        return HttpResponse(status=200)
    else:
        if result=='correct':
            if id in request.session['answer']:
                print('cheater')
                response = False
                return HttpResponse(response)
            request.session['answer'][answer_id] = 1
            print(request.session['answer'])
            return HttpResponse(status=200)
        else:
            if id in request.session['answer']:
                print('cheater')
                response = False
                return HttpResponse(response)
            request.session['answer'][answer_id] = 0
            print(request.session['answer'])
            return HttpResponse(status=200)

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
        messages.error(
            request, 'Quiz could not be updated. \
                Try again.')
        return redirect(reverse('quiz'))
    form = add_quizForm(instance=quiz)
    context = {
        'form': form,
        'quiz': quiz,
        }
    return render(request, 'quiz/update_quiz.html', context)

def questionnaire(request, quiz_id, num=0):
    """View to view Questionnaire"""
    question_id=[]
    request.session.modified = True
    questions = Questions.objects.all().filter(quiz=quiz_id)
    for question in questions:
        question_id.append(question.id)
    final = len(question_id)
    if num==0 and 'answer' not in request.session:
        print('new session')
        request.session['answer']= {}
        print(request.session['answer'])
    quiz = get_object_or_404(Quiz, id=quiz_id)
    actual_question = get_object_or_404(Questions, id=question_id[num])
    crypt= {
        "A": randon_word(6),
        "B": randon_word(6),
        "C": randon_word(6),
        "D": randon_word(6),
        "id": actual_question.id,
        'length': final,
        }
    answer = crypt[actual_question.answer]
    context = {
        'crypt': json.dumps(crypt),
        'answer': answer,
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

def delete_question(request, question_id):
    """View to delete question"""
    if not request.user.is_superuser:
        messages.error(request, 'Permision Denied!.')
        return redirect(reverse('home'))
    question = get_object_or_404(Questions, id=question_id)
    question.delete()
    messages.success(request, 'Questions deleted!')
    return redirect(reverse('quiz'))

def update_question(request, question_id):
    """View to update quiz name"""
    question_list=[]
    if not request.user.is_superuser:
        messages.error(request, 'Permision Denied!.')
        return redirect(reverse('home'))
    question = get_object_or_404(Questions, id=question_id)
    all_questions = Questions.objects.all()
    for questions in all_questions:
        question_list.append(questions.id)
    if request.method == 'POST':
        form = add_questionForm(request.POST, request.FILES, instance=question)
        if form.is_valid():
            form.save()
            messages.success(request, 'Question updated!')
            return redirect(reverse(
                'questionnaire', args=[question.quiz.id, question_list.index(question.id)]))
        messages.error(
            request, 'Question could not be updated. \
                Try again.')
        return redirect(reverse('quiz'))
    form = add_questionForm(instance=question)
    context = {
        'question': question,
        'form': form,
        }
    return render(request, 'quiz/update_question.html', context)

def results(request):
    """View to show resulst"""
    correct_answers = 0
    if 'answer' in request.session:
        answers  = request.session['answer']        
        for key, value in answers.items():
            if value == 1:
                correct_answers+=1
        final_results = math.floor(correct_answers/len(answers) * 100)
        del request.session['answer']
    if 'employee' in request.session:
        employee = request.session['employee']
        staff = get_object_or_404(Staff, employee_number=employee['employee'])
        del request.session['employee']
    
    context = {
        'results': final_results,
        'staff': staff,
    }
    return render(request, 'quiz/results.html', context)
