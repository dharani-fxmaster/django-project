from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Transaction
from django.views.generic import TemplateView,CreateView,DeleteView,UpdateView,ListView

class HomeView(TemplateView):
    template_name = "home.html"

class TransactionListView(ListView):
    model = Transaction
    template_name = "transaction_list.html"                 
    context_object_name = "transactions" 
    ordering = ['-transaction_date']

class TransactionCreateView(CreateView):
    model = Transaction
    fields = ['user','transaction_title','amount','description']
    template_name = "transaction_create.html"
    success_url = reverse_lazy('transaction_list')


class TransactionUpdateView(UpdateView):
    model = Transaction
    fields = ['user', 'amount','description', 'transaction_types']
    template_name = "transaction_update.html"
    success_url = reverse_lazy('transaction_list')

class TransactionDeleteView(DeleteView):
    model = Transaction
    template_name = "transaction_delete.html"
    success_url = reverse_lazy('transaction_list')




