from django.db import models
from django.contrib.auth.models import AbstractUser

# models.py

from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
#... any other imports

class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)

class User(AbstractUser):
    email = models.EmailField('Email', unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()

#_______________
from email.policy import default
from django.db import models


class Book(models.Model):
    SIZE_CHOICES = [
        ('small', 'Small'),
        ('medium', 'Medium'),
        ('large', 'Large'),
    ]
    
    CRUST_CHOICES = [
        ('normal', 'Normal'),
        ('thin', 'Thin'),
        ('thick', 'Thick'),
        ('gluten_free', 'Gluten Free'),
    ]
    
    SAUCE_CHOICES = [
        ('tomato', 'Tomato'),
        ('bbq', 'BBQ'),
    ]
    
    CHEESE_CHOICES = [
        ('mozzarella', 'Mozzarella'),
        ('vegan', 'Vegan'),
        ('low_fat', 'Low Fat'),
    ]
    
    TOPPING_CHOICES = [
        ('pepperoni', 'Pepperoni'),
        ('chicken', 'Chicken'),
        ('ham', 'Ham'),
        ('pineapple', 'Pineapple'),
        ('peppers', 'Peppers'),
        ('mushrooms', 'Mushrooms'),
        ('onions', 'Onions'),
    ]


    size = models.CharField(max_length=10, choices=SIZE_CHOICES, default='medium')
    crust_type = models.CharField(max_length=20, choices=CRUST_CHOICES, default='normal')
    sauce = models.CharField(max_length=10, choices=SAUCE_CHOICES, default='tomato')
    cheese = models.CharField(max_length=20, choices=CHEESE_CHOICES, default='mozzarella')
    toppings = models.CharField(max_length=20, choices=TOPPING_CHOICES, default='pepperoni')
    

class Pay(models.Model):
    
    name_on_card = models.CharField(max_length=100)
    card_number = models.CharField(max_length=16)
    expiry_date = models.CharField(max_length=5)
    cvc = models.CharField(max_length=4)
