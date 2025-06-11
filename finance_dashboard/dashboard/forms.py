from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import EMI, Budget, Expense, Goal

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class EMIForm(forms.ModelForm):
    class Meta:
        model = EMI
        fields = ['loan_amount', 'interest_rate', 'tenure_months', 'loan_name', 'issuing_bank']

class BudgetForm(forms.ModelForm):
    class Meta:
        model = Budget
        fields = ['income', 'rent', 'groceries', 'utilities', 'miscellaneous', 'month', 'year']

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['category', 'amount', 'record_month', 'record_year']

class GoalForm(forms.ModelForm):
    class Meta:
        model = Goal
        fields = ['name', 'target_amount', 'saved_amount', 'deadline']
