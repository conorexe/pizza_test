from django.contrib import admin
from .models import *
from .forms import *

# Register your models here.
admin.site.register(Book)
admin.site.register(User)
admin.site.register(Pay)




