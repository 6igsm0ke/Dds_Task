from django.shortcuts import render
from app.models import *
from rest_framework.viewsets import ModelViewSet
from app.serializers import *

# Вьюшки для моделек чтобы создать ендпойнты

# Create your views here.
class TransactionViewSet(ModelViewSet):
    serializer_class = TransactionSerializer
    queryset = Transaction.objects.all()
    lookup_field = "uuid"


class StatusViewSet(ModelViewSet):
    serializer_class = StatusSerializer
    queryset = Status.objects.all()
    lookup_field = "uuid"


class TransactionTypeViewSet(ModelViewSet):
    serializer_class = TransactionTypeSerializer
    queryset = TransactionType.objects.all()
    lookup_field = "uuid"


class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    lookup_field = "uuid"


class SubCategoryViewSet(ModelViewSet):
    serializer_class = SubCategorySerializer
    queryset = SubCategory.objects.all()
    lookup_field = "uuid"
