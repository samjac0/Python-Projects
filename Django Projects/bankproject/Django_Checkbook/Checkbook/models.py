from django.db import models

# Create your models here.
class Account(models.Model):
    First_name = models.CharField(max_length=60, default="", blank=True, null=False)
    Last_name = models.CharField(max_length=60, default="", blank=True, null=False)
    Initial_deposit = models.DecimalField(default=0.00, max_digits=10000,decimal_places=2)

    Accounts = models.Manager()

    def __str__(self):
        return self.First_name + ' ' + self.last_name

transactionTypes = [('Deposit', 'Deposit'), ('Withdrawal', 'Withdrawal')]

class Transaction(models.Model):
    Date = models.DateField()
    Account = models.ForeignKey(Account, on_delete=models.CASCADE)
    Description = models.TextField(max_length=200, default="", blank=True, null=False)
    Amount = models.DecimalField(default=0.00, max_digits=15, decimal_places=2)
    Type = models.CharField(max_length=10, choices=transactionTypes)

    Transactions = models.Manager()

