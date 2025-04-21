from .views import *
from rest_framework.routers import DefaultRouter
from django.urls import path, include

app_name = "app"

router = DefaultRouter()
router.register("transactions", TransactionViewSet, "transaction")
router.register("statuses", StatusViewSet, basename="status")
router.register("transaction_types", TransactionTypeViewSet, basename="transaction_type")
router.register("categories", CategoryViewSet, basename="category")
router.register("subcategories", SubCategoryViewSet, basename="subcategory")
urlpatterns = router.urls

urlpatterns += [
    path("home/", index_view, name="index"),
    path('create/', transaction_create_view, name='create_transaction'),
    path('dictionaries/', manage_dictionaries_view, name='manage_dictionaries'),
    path("edit/<uuid:uuid>/", transaction_edit_view, name="edit_transaction"),
    path("delete/<uuid:uuid>/", transaction_delete_view, name="delete_transaction"),
    path("get-categories/", get_categories_by_type, name="get_categories_by_type"),
    path("get-subcategories/", get_subcategories_by_category, name="get_subcategories_by_category"),
    path('dictionaries/edit/<str:model>/<int:pk>/', edit_dictionary_item, name='edit_dictionary_item'),
    path('dictionaries/delete/<str:model>/<int:pk>/', delete_dictionary_item, name='delete_dictionary_item'),
]
