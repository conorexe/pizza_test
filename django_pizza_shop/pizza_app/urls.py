from django.urls import path
from . import views
from .forms import *

urlpatterns = [
   path('', views.index, name="index"),
   path('register/', views.UserSignupView.as_view(), name="register"),
   path('login/',views.LoginView.as_view(template_name="login.html", authentication_form=UserLoginForm)),
   path('logout/', views.logout_user, name="logout"),
   path('login/create/', views.create_book, name="create_book"),
   path('payment/', views.process_payment, name="payment"),
   path('payment_sucess/', views.payment_success, name="payment_success")
]