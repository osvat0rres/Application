
from django.urls import path
from . import views

urlpatterns = [
    path('expenses/', views.ExpensesListCreateView.as_view()),
    path('total/', views.ExpensesTotalView.as_view())
]