from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title =  models.CharField(max_length=255, default="Default Title")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    description = models.TextField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()

    def __str__ (self):
        return self.title
    
