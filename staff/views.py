from django.shortcuts import (
    render, redirect, reverse, get_object_or_404)
from django.contrib import messages
from django.db.models import Q
from .models import Staff
from quiz.models import Results
from .forms import add_staffForm


# Create your views here.
def staff(request):
    """ A view to return all staff info """
    if not request.user.is_superuser:
        messages.error(request, 'Permision Denied!.')
        return redirect(reverse('home'))

    if 'q' in request.GET:
        query = request.GET['q']
        if not query:
            return redirect(reverse('staff'))
        all_staff = Staff.objects.all().order_by('employee_number')
        queries = Q(first_name__icontains=query) | Q(last_name__icontains=query)
        query_staff = all_staff.filter(queries)
        context = {
            'all_staff': query_staff,
        }
        return render(request, 'staff/staff.html', context)
    all_staff = Staff.objects.all().order_by('employee_number')
    context = {
        'all_staff': all_staff,
    }

    return render(request, 'staff/staff.html', context)

def add_staff(request):
    """ A view to add staff """
    if not request.user.is_superuser:
        messages.error(request, 'Access Denied!')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = add_staffForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Staff Added!')
            return redirect(reverse('staff'))
        messages.error(
            request, 'Staff could not be added!')
        new_form = add_staffForm()

        context = {
            'errors': form.errors.values(),
            'form': new_form,
            }
        return render(request, 'staff/add_staff.html', context)

    form = add_staffForm()
    context = {
        'form': form,
        }
    return render(request, 'staff/add_staff.html', context)

def delete_staff(request, staff_id):
    """ A view to update staff details"""
    if not request.user.is_superuser:
        messages.error(request, 'Access Denied!')
        return redirect(reverse('home'))
    staff = get_object_or_404(Staff, id=staff_id)
    staff.delete()
    messages.success(request, 'Staff record deleted!')
    return redirect(reverse('staff'))

def quiz_results(request):
    all_results = Results.objects.all()
    context = {
        'results': all_results,
    }
    return render(request, 'staff/quiz_results.html', context)
