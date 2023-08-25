from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib import messages

from items.models import *
from .forms import SignupForm


# Create your views here.
def index(request):
    items = Item.objects.filter(is_sold=False)[0:9]
    categories = Category.objects.all()

    context = {
        'categories': categories,
        'items': items
    }

    return render(request, 'index.html', context)


def contact(request):
    return render(request, 'contact.html')


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SignupForm()

    context = {
        'form': form
    }

    return render(request, 'signup.html', context)


# logout function
# def logout_request(request):
#     logout(request)
#     messages.info(request, "You have logged out!!")
#     return redirect('core:index')
