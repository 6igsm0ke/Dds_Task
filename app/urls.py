from .views import *
from rest_framework.routers import DefaultRouter
from django.urls import path

app_name = "app"

router = DefaultRouter()
router.register("transactions", TransactionViewSet, "transactions")
urlpatterns = router.urls

urlpatterns += []