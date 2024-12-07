from django.urls import path
from .import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.expense_list, name='expense_list'),
    path('add/', views.add_expense, name='add_expense'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('categories/', views.category_list, name="category_list"),
    path('categories/add/', views.add_category, name="add_category"),


]
