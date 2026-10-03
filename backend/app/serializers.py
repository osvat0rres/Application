from rest_framework import serializers
from .models import User,Catergory, Expense, RecurringExpense


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "first_name",
            "last_name",
        ]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Catergory
        fields = [
            "id",
            "user",
            "name",
        ]


class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = [
            "id",
            "user",
            "category",
            "title",
            "amount",
            "description",
            "date",
            "created_at",
            "updated_at",
        ]
        read_only_fields = [
            "id",
            "user",
            "created_at",
            "updated_at",
        ]


class RecurringExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecurringExpense
        fields = [
            "id",
            "user",
            "category",
            "title",
            "amount",
            "frequency",
            "start_date",
            "next_date",
        ]
        read_only_fields = [
            "id",
            "user",
        ]
      
