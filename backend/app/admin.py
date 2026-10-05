from django.contrib import admin
from app.models import User, Expenses

# Register your models here.

admin.site.register(Expenses)
admin.site.register(User)
