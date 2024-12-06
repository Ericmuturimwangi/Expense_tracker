from django.shortcuts import render
from .models import Expense
from .forms import ExpenseForm
from django.shortcuts import redirect


def expense_list(request):
    expenses = Expense.objects.filter(user = request.user)
    return render(request, 'expense/expense_list.html', {'expense': expenses})

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
    return render (request, 'expense/add_expense.html', {'form':form})

