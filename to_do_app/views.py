from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import ToDoItem, ToDoList
from django.shortcuts import render
def index(request):
    return HttpResponse("Hello, world")

def homepage(request, id):
    obj = get_object_or_404(ToDoItem, pk=id)
    context = {
        "obj" : obj
    }
    return render(request, "to_do_app/index.html", context)

def display(request):
    obj = ToDoItem.objects.all()
    context = {
        "obj" : obj
    }
    return render(request, "to_do_app/index.html", context)