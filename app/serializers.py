from .services import validate_subcategory_and_category, validate_category_and_type
from .models import *
from rest_framework import serializers


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ["uuid", "name"]


class TransactionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionType
        fields = ["uuid", "name"]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["uuid", "name"]


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = ["uuid", "name", "category"]

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["category"] = CategorySerializer(instance.category).data
        return data


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = [
            "uuid",
            "name",
            "date",
            "status",
            "type",
            "category",
            "subcategory",
            "amount",
            "comment",
        ]
        
        extra_kwargs = {
            "amount": {"required": True},
            "type": {"required": True},
            "category": {"required": True},
            "subcategory": {"required": True},
        }

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["status"] = StatusSerializer(instance.status).data
        data["type"] = TransactionTypeSerializer(instance.type).data
        data["category"] = CategorySerializer(instance.category).data
        data["subcategory"] = SubCategorySerializer(instance.subcategory).data
        return data

    def validate(self, data):
        validate_subcategory_and_category(data["category"], data["subcategory"])
        validate_category_and_type(data["category"], data["type"])
        return data
