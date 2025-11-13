from django.db import models

from django.db import models
from django.contrib.auth.models import User

class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    transaction_title = models.CharField(max_length=50,default="Untitled")
    transaction = [('CR','Credit'),('DR', 'Debit')]
    transaction_types = models.CharField(max_length=2, choices=transaction, default='CR',)
    transaction_date = models.DateField(blank=True, null=True)

    class Meta:
        permissions = [("can_edit_transaction", "Can Edit Transaction"),
                       ("can_approve_transaction","Can approve transaction"),]
    
    def __str__(self):
        return f"{self.user.username} - {self.amount}"

