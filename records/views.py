from rest_framework import viewsets, permissions
from .models import Transaction
from .serializers import TransactionSerializers
from .permissions import IsAdminOrReadOnly

class TransactionViewSet(viewsets.ModelViewSet):
    serializer_class = TransactionSerializers
    permission_classes = [IsAdminOrReadOnly]

    def get_querysert(self):
        #Users can only see their own records 
        #return Transaction.objects.all() if Admins see everything

        return Transaction.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        # Automatically assign the loggen-in user to the record
        serializer.save(user=self.request.user)
        
