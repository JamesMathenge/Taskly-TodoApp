from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import TodoForm
from .models import Todo

def index(request):
    item_list = Todo.objects.order_by("-created_at") 
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Task added successfully.")  
            return redirect('taskly')
    else:
        form = TodoForm()  # Empty form for GET requests
    page = {
        "form": form,  
        "list": item_list,
        "title": "To-Do List",  
    }
    return render(request, 'taskly/index.html', page)

def remove(request, item_id):
    item = get_object_or_404(Todo, id=item_id)  
    item.delete()
    messages.success(request, "Task removed successfully.") 
    return redirect('taskly')