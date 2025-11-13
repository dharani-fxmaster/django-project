from django.urls import path
from .views import TransactionCreateView, transactions_list

urlpatterns = [
    path('transactions/', transactions_list, name='transaction_list'),           # e.g., list or homepage for transactions
    path('create/', TransactionCreateView.as_view(), name='transaction_create'),
]
