from django.shortcuts import render
from .models import *
from rest_framework.viewsets import ModelViewSet
from .serializers import TransactionSerializer

# Create your views here.
class TransactionViewSet(ModelViewSet):
    serializer_class = TransactionSerializer
    queryset = Transaction.objects.all()
    lookup_field='uuid'