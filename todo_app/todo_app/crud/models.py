from django.db import models

# Create your models here.
class TodoListItems(models.Model):
    content=models.TextField()