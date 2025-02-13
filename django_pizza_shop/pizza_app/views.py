from django.shortcuts import render
from django.http import HttpResponse

#_____________
import re
from django.shortcuts import render, get_object_or_404
import random
from .models import *
from .forms import *
from django.views.generic import CreateView
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'index.html')

from django.views.generic import CreateView
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import * 

class UserSignupView(CreateView):
    model = User
    form_class = UserSignupForm
    template_name = 'user_signup.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')
    
    
from django.contrib.auth.views import LoginView

class UserLoginView(LoginView):
    template_name='login.html'


def logout_user(request):
    logout(request)
    return redirect("/login/create")

#__________________

def create_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            new_book = form.save()
            return redirect("/payment")
        else:
            return render(request, 'create_book.html', {'form':form})
    else:
    #     # its a GET request
    #     # load a new instance of the BookForm 
    #     # show it to the user
        form = BookForm()
        return render(request, 'create_book.html', {'form': form})
    
    
    

# views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import Pay1


def process_payment(request):
    
    if request.method == 'POST':
        form = Pay1(request.POST)
        if form.is_valid():
            
            new_pay = form.save()
            
            # Process payment here (e.g., record payment in the database)
            messages.success(request, 'Payment successful.')
            return redirect('payment_success')
    else:
        form = Pay1()
    return render(request, 'payment.html', {'form': form})


def payment_success(request):
    return render(request, 'payment_success.html')