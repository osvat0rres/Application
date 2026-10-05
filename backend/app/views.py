from django.shortcuts import get_object_or_404
from .serializers import ExpensesSerializer, ExpensesReturnSerializer
from app.models import Expenses
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics
from django.db import models
from rest_framework.permissions import IsAdminUser,AllowAny, IsAuthenticated



class ExpensesListCreateView(generics.ListCreateAPIView):
    queryset = Expenses.objects.all()
    serializer_class = ExpensesSerializer
    permission_classes = [IsAuthenticated]
    
    def get_total_exepenses(self):
        total_expenses = self.get_queryset().aggregate(total=models.Sum('amount'))['total']
        return total_expenses if total_expenses is not None else 0
    
    
    
    
class ExpensesTotalView(generics.ListAPIView):
    serializer_class = ExpensesReturnSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Expenses.objects.filter(user=self.request.user)
    
    def get_total_expenses(self):
        total_expenses = self.get_queryset().aggregate(
            total=models.Sum("spend")
        )["total"]
        
        return total_expenses if total_expenses is not None else 0

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)

        return Response({
            "total_expenses": self.get_total_expenses(),
            "expense": serializer.data
        })
        
        
