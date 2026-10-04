from django.shortcuts import get_object_or_404
from .serializers import ExpensesSerializer, ExpensesReturnSerializer
from app.models import Expenses
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics



class ExpensesListCreateView(generics.ListCreateAPIView):
    queryset = Expenses.objects.all()
    serializer_class = ExpensesSerializer
    
    

    
