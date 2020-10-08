from rest_framework import serializers
from APIDemo.models import Todo


class ToDoSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'title',
            'description'
        )
        model = Todo
