from django.db import models
from django.utils.translation import gettext as _
from .core import BaseModel


# Create your models here.
class Status(BaseModel):
    name = models.CharField(_("Name of Status"), max_length=256)

    def __str__(self):
        return self.name


class TransactionType(BaseModel):
    name = models.CharField(_("Name of type"), max_length=256)

    def __str__(self):
        return self.name


class Category(BaseModel):
    name = models.CharField(_("Name of category"), max_length=256)

    def __str__(self):
        return self.name


class SubCategory(BaseModel):
    category = models.ForeignKey(Category, related_name='subcategories', on_delete=models.SET_NULL, blank=True, null=True)
    name = models.CharField(_("Name of subcategory"), max_length=256)

    def __str__(self):
        return self.name


class Transaction(BaseModel):
    name = models.CharField(_("Name of transaction"), max_length=256)
    date = models.DateField(
        _("Date of transaction"), auto_now=False, auto_now_add=False
    )
    status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True)
    type = models.ForeignKey(TransactionType, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    subcategory = models.ForeignKey(
        SubCategory, on_delete=models.SET_NULL, null=True, blank=True
    )
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    comment = models.TextField(_("Comment about transaction"), blank=True, null=True)
