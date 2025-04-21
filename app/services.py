from django.forms import ValidationError


def validate_subcategory_and_category(category, subcategory):
    if subcategory.category != category:
        raise ValidationError("Подкатегория не относится к выбранной категории.")
    
def validate_category_and_type(category, trans_type):
    if category.type != trans_type:
        raise ValidationError("Категория не относится к выбранному типу.")