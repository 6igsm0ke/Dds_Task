from django import forms
from .models import Transaction
from .services import validate_subcategory_and_category, validate_category_and_type


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['name', 'date', 'status', 'type', 'category', 'subcategory', 'amount', 'comment']

    def clean(self):
        cleaned_data = super().clean()

        category = cleaned_data.get("category")
        subcategory = cleaned_data.get("subcategory")
        type_ = cleaned_data.get("type")

        if category and subcategory:
            try:
                validate_subcategory_and_category(category, subcategory)
            except ValueError as e:
                self.add_error('subcategory', str(e))

        if category and type_:
            try:
                validate_category_and_type(category, type_)
            except ValueError as e:
                self.add_error('category', str(e))

        return cleaned_data