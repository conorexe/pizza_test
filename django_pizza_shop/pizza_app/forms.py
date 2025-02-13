# forms.py
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ModelForm, ModelChoiceField
from .models import User
from django.db import transaction

class UserSignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_admin = False
        user.email = self.cleaned_data['username']
        user.save()
        return user
    
    
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        
        
#---------------------

from .models import *
from django import forms

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [ 'size', 'crust_type', 'sauce', 'cheese', 'toppings' ]
        
        
        

from django import forms

from .models import Pay

class Pay1(forms.ModelForm):
    class Meta:
        model = Pay
        fields = ['name_on_card', 'card_number', 'expiry_date', 'cvc', 'name', 'address']

    name = forms.CharField(max_length=100)
    address = forms.CharField(max_length=255)


