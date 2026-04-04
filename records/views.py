from rest_framework import viewsets, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Sum, Count
from .models import Transaction
from .serializers import TransactionSerializers
from .permissions import IsAdminOrReadOnly, IsAnalystOrAdmin


class DashboardSummaryView(APIView):
    permission_classes = [IsAnalystOrAdmin]

    def get(self, request):
        #performing the aggregation in the db, not in python memory

        data = Transaction.objects.aaggregate(
            total_income=sum('amount', filter=models.Q(type='income')),
            total_expenses = Sum('amount', filter=models.Q(type='expense')),
            total_records = Count('id')

        )

        #Calculate Net Balance
        income = data['total_income'] or 0
        expenses = data['total_expenses'] or 0
        data['net_balance']=income - expenses

        return Response(data)



class TransactionViewSet(viewsets.ModelViewSet):
    serializer_class = TransactionSerializers
    permission_classes = [IsAdminOrReadOnly]


    queryset = Transaction.objects.all()

    def get_querysert(self):
        #Users can only see their own records 
        #return Transaction.objects.all() if Admins see everything

        return self.queryset.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        # Automatically assign the loggen-in user to the record
        serializer.save(user=self.request.user)

