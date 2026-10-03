from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.conf import settings

# Create your models here.

class User(AbstractBaseUser, models.Model):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    USERNAME_FIELD = "email"
    
    def __str__(self):
        return self.email
    

class Catergory(models.Model):
    CATEGORY_CHOICE = [
        ("Rent", "Rent"),
    ("Entertainment", "Entertainment"),
    ("Groceries", "Groceries"),
    ("Gas", "Gas"),
    ("Utilities", "Utilities"),
    ("Bills", "Bills"),
    ]
    user =models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="categories")
    name = models.CharField(max_length=100, choices=CATEGORY_CHOICE)
    
class Expense(models.Model):
    user = models.ForeignKey( settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="expenses")
    category = models.ForeignKey(Catergory, on_delete=models.SET_NULL, null=True, related_name="expenses")
    title = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return f"{self.title} - {self.amount}"
    
class RecurringExpense(models.Model):
    frequncy = [
          ("Weekly", "Weekly"),
    ("Monthly", "Monthly"),
    ("Yearly", "Yearly"),
    ]
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="recurring_expenses")
    category = models.ForeignKey(Catergory, on_delete=models.CASCADE, related_name="recurring_expenses")
    title = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    frequncy = models.CharField(max_length=20, choices=frequncy)
    start_date = models.DateField()
    next_date = models.DateField()
    
    def __str__(self):
        return f"{self.title} - ${self.amount}"
    
    
    
