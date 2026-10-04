from rest_framework import serializers
from .models import Expenses

class ExpensesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expenses
        fields = (
            'user',
            'title',
            'category',
            'spend',
            'description',
            'spend_date',
            'created_at'
        )
    def validate_price(self,value):
        if value <= 0:
            raise serializers.ValidationError(
                "Spend most be grated then 0."
            )
        return value

class ExpensesReturnSerializer(serializers.ModelSerializer):
    expense = ExpensesSerializer(many=True, read_only=True)
    
    class Meta:
        model = Expenses
        fields = ("user", "title", "category","spend", "spend_date", "description") 
