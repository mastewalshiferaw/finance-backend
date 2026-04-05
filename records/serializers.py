from rest_framework import serializers
from .models import Transaction


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'
        read_only_fields = ['user'] #automatically a user will be set automatically in the view

        def validate_amount(self, value):
            if value <=0:
                raise serializers.ValidationError("Amount must be a positive number.")
            return value