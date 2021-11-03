from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .models import Staff
# Create your views here.
def staff(request):
    """ A view to return all staff info """
    if not request.user.is_superuser:
        messages.error(request, 'Permision Denied!.')
        return redirect(reverse('home'))

    all_staff = Staff.objects.all()
    context = {
        'all_staff': all_staff,
    }
    return render(request, 'staff/staff.html', context)
