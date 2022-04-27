from django.db import models

# Create your models here.
class Account(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    initial_deposit = models.DecimalField(default= 0.00, max_digits=15,decimal_places=2)

    Accounts = models.Manager()

    def __str__(self):
        return self.first_name + ' ' + self.last_name

TransactionTypes = [('Deposit', 'Deposit'), ('Withdrawal', 'Withdrawal')]

class Transaction(models.Model):
    date = models.DateField()
    type = models.CharField(max_length=10, choices=TransactionTypes)
    amount = models.DecimalField(default=0.00, max_digits=15, decimal_places=2)
    description = models.TextField(max_length=200, default="", blank=True, null=False)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)

    Transactions = models.Manager()

