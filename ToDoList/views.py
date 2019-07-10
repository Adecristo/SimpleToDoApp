from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoItem

# Create your views here.
def ToDoView (request):
    all_items = ToDoItem.objects.all()
    return render(request, 'base.html',{'all_items' : all_items})