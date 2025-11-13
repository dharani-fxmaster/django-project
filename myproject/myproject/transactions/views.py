from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Transactions

# Home or list view
def home_view(request):
    return render(request, "home.html")

def transactions_list(request):
    transactions = Transactions.objects.all()
    return render(request, "transactions/transactions_list.html", {"transactions": transactions})

# Create View
class TransactionCreateView(CreateView):
    model = Transactions
    fields = ['transaction_types', 'transaction_date']
    template_name = "transactions/transaction_form.html"
    success_url = reverse_lazy("transaction_list")
