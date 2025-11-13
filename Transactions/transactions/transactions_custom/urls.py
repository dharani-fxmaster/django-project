from django.urls import path
from . import views
from .views import HomeView,TransactionListView,TransactionCreateView,TransactionCreateView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('transactions/',views.TransactionListView.as_view(),name='transaction_list'),
    path('transactions/add/',views.TransactionCreateView.as_view(),name='transaction_add'),
    path('transactions/update/<int:pk>/',views.TransactionUpdateView.as_view(),name='transaction_update'),
    path('transactions/delete/<int:pk>/',views.TransactionDeleteView.as_view(),name='transaction_delete'),
    ]