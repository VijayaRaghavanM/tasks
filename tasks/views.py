from django.shortcuts import render, HttpResponse, redirect, reverse
from .models import Task
from django.contrib import messages

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return redirect(reverse('login'))
    tasks = Task.objects.filter(author=request.user)
    context = {"tasks": tasks}
    return render(request, "tasks/index.html", context)

def new(request):
    name = request.GET.get('name', '')
    if name == '':
        messages.add_message(request, messages.INFO, 'Cannot create Empty Task')
    else:
        task = Task.objects.create(author=request.user, name=name)
    return redirect(reverse("tasks:index"))    

def delete(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return redirect(reverse("tasks:index"))    

def update(request, pk):
    task = Task.objects.get(id=pk)
    if request.method == 'POST':
        name = request.POST.get('name','')
        if name == '':
            messages.add_message(request, messages.INFO, 'Cannot create Empty Task')
        else:
            task.name = name
            task.save()
        return redirect(reverse('tasks:index'))
    context = {"task": task}
    return render(request, "tasks/update.html", context)