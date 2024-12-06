from django.shortcuts import render
from .models import Expense
from .forms import ExpenseForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required


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

