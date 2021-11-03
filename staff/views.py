from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .models import Staff
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
