from django.contrib import admin

# Register your models here.

from .models import TodoListItems
admin.site.register(TodoListItems)