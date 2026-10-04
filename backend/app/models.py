from django.db import models   
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass


class Expenses(models.Model):
    category_choices =[
        ("bills", "Bills"),
        ("entertainment", "Entertainment"),
        ("gas", "Gas"),
        ("rent","Rent"),
        ("utilities", "Utilities"),
        ("credit card", "Credit Card"),
        ("other", "Other")
    ]
    # I just added the "null=True", and the black tre for now becouse it is not going to requiere
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length = 100)
    category = models.CharField(max_length=30, choices=category_choices)
    spend = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(max_length=500)
    spend_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add = True)
    
    
    @property
    def amount(self):
        return self.spend > 0
    
    def __str__(self):
        return f"Expense: {self.user}: {self.title} ${self.spend}"
    
    
    
