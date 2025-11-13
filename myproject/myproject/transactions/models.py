from django.db import models

# Create your models here.
class Transactions(models.Model):
    transaction = [('CR','Credit'),('DR', 'Debit')]
    transaction_types = models.CharField(max_length=2, choices=transaction)
    transaction_date = models.DateField(blank=True, null=True)

