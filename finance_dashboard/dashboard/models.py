from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class EMI(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    loan_name = models.CharField(max_length=100, default='Personal Loan')
    issuing_bank = models.CharField(max_length=100, default='Unknown Bank')
    loan_amount = models.FloatField(default=0)
    interest_rate = models.FloatField(default=10.0)  # annual interest %
    tenure_months = models.IntegerField(default=12)
    emi_amount = models.FloatField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"{self.loan_name} ({self.user.username})"


class Budget(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    income = models.FloatField(default=0)
    rent = models.FloatField(default=0)
    groceries = models.FloatField(default=0)
    utilities = models.FloatField(default=0)
    miscellaneous = models.FloatField(default=0)
    month = models.IntegerField(default=1)
    year = models.IntegerField(default=timezone.now().year)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"Budget for {self.month}/{self.year} - {self.user.username}"


class Expense(models.Model):
    CATEGORY_CHOICES = [
        ('Rent', 'Rent'),
        ('Groceries', 'Groceries'),
        ('Utilities', 'Utilities'),
        ('Miscellaneous', 'Miscellaneous'),
        ('Entertainment', 'Entertainment'),
        ('Transport', 'Transport'),
        ('Health', 'Health'),
        ('Education', 'Education'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='Miscellaneous')
    amount = models.FloatField(default=0)
    record_month = models.CharField(max_length=20, default=timezone.now().strftime("%B"))
    record_year = models.IntegerField(default=timezone.now().year)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"{self.category} ₹{self.amount} ({self.record_month}/{self.record_year})"


class Goal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, default="Untitled Goal")
    target_amount = models.FloatField(default=0)
    saved_amount = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    deadline = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.name} for {self.user.username}"