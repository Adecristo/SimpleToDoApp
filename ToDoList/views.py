from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import ToDoItem

# Create your views here.
def ToDoView (request):
    all_items = ToDoItem.objects.all()
    return render(request, 'base.html',{'all_items' : all_items})

def AddItem(request):
    AddedItem = ToDoItem(Content = request.POST['Content'])
    AddedItem.save()
    return HttpResponseRedirect('/home/')
    
def DeleteItem(request,item_id):
    DelItem = ToDoItem.objects.get(id=item_id)
    DelItem.delete()
    return HttpResponseRedirect('/home/')