from rest_framework import filters, generics, viewsets
from app.models import Catergory, User, Expense, RecurringExpense
from app.serializers import CategorySerializer, UserSerializer, ExpenseSerializer, RecurringExpenseSerializer
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework import status

class UserView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    
    
class ExpenseView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        expenses = Expense.objects.filter(user=request.user)

        serializer = ExpenseSerializer(
            expenses,
            many=True
        )

        return Response(serializer.data)

    def post(self, request):
        serializer = ExpenseSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(user=request.user)

            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
