from django.shortcuts import render, redirect
from django.contrib.auth import logout, views
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin

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


class ResetPasswordView(SuccessMessageMixin, views.PasswordResetView):
    template_name = 'password_reset.html'
    email_template_name = 'password_reset_email.html'
    subject_template_name = 'password_reset_subject'
    success_message = ("We've emailed you instructions for setting your password. \""
                       "If an account exists with the email you entered, you'll receive them shortly. \
                       If you don't receive an email, please make sure you've entered the email you registered with, \
                       and check your spam folder.")
    success_url = reverse_lazy('login')
