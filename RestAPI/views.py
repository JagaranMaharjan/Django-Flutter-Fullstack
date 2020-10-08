
from django.shortcuts import render

# Create your views here.
from rest_framework import generics

from APIDemo.models import Todo
from .serializers import ToDoSerializer


class ListToDo(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = ToDoSerializer


class DetailToDo(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = ToDoSerializer
