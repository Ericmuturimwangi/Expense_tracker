from django.shortcuts import render
from .models import Expense, Category
from .forms import ExpenseForm, CategoryForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.db import models


# @login_required
def expense_list(request):
    if request.user.is_authenticated:
        expenses = Expense.objects.filter(user = request.user)
    else:
        expenses = []
    
    return render(request, 'expense_list.html', {'expense': expenses})

def add_expense(request):
    if request.method == "POST":
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user
            expense.save()
            return redirect('expense_list')
    else:
        form = ExpenseForm()
    return render (request, 'add_expense.html', {'form':form})

# registration view
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('expense_list')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form':form})

@login_required
def add_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.user = request.user
            category.save()
            return redirect('category_list')

        
    else:
        form = CategoryForm()
    return render (request, 'add_category.html', {'form': form})

@login_required
def category_list(request):
    categories = Category.objects.filter(user=request.user)
    totals = {category: Expense.objects.filter(user=request.user, category=category).aggregate(models.Sum('amount'))['amount__sum'] or 0 for category in categories}
    context={'categories':categories, 'totals':totals}
    return render(request, 'category_list.html', context)