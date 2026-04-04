from rest_framework import viewsets, views, response
from django.db.models import Sum, Count, Q
from .models import Transaction
from .serializers import TransactionSerializer
from .permissions import IsAdminOrReadOnly, IsAnalystOrAdmin

class TransactionViewSet(viewsets.ModelViewSet):
    serializer_class = TransactionSerializer
    permission_classes = [IsAdminOrReadOnly]
    queryset = Transaction.objects.all()

    def get_queryset(self): return self.queryset.filter(user=self.request.user)
    def perform_create(self, serializer): serializer.save(user=self.request.user)

class DashboardSummaryView(views.APIView):
    permission_classes = [IsAnalystOrAdmin]
    def get(self, request):
        data = Transaction.objects.filter(user=request.user).aggregate(
            total_income=Sum('amount', filter=Q(type='income')),
            total_expenses=Sum('amount', filter=Q(type='expense')),
            total_records=Count('id')
        )
        data['net_balance'] = (data['total_income'] or 0) - (data['total_expenses'] or 0)
        return response.Response(data)