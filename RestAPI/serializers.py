from rest_framework import serializers
from APIDemo.models import Todo


# created format of json data
class ToDoSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'title',
            'description'
        )
        model = Todo
