from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .models import Staff
from .forms import add_staffForm
from django.db.models import Q

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
        all_staff = Staff.objects.all()
        queries = Q(first_name__icontains=query) | Q(last_name__icontains=query)
        query_staff = all_staff.filter(queries)
        context = {
            'all_staff': query_staff,
        }
        return render(request, 'staff/staff.html', context)         
    all_staff = Staff.objects.all()
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
        else:
            messages.error(
                request, 'Staff could not be added. \
                    Please ensure the form is valid.')
            return redirect(reverse('add_staff'))

    form = add_staffForm()
    print(form)
    context = {
        'form': form,
        }
    return render(request, 'staff/add_staff.html', context)
