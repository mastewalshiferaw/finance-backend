from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TransactionViewSet, DashboardSummaryView

router = DefaultRouter()
router.register(r'transactions', TransactionViewSet, basename='transaction')

urlpatterns = [
    path('', include(router.urls)),
    path('summary/', DashboardSummaryView.as_view(), name='dashboard-summary'),
]