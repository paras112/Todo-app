from rest_framework import serializers
from .models import TodoListItems

class CrudSerializers(serializers.ModelSerializer):
    class Meta:
        model = TodoListItems
        fields = ["pk","content"]