from django.shortcuts import render, redirect
from .models import Todo

def home(request):
    if request.method == "POST":
        title = request.POST.get("title")

        if title:
            Todo.objects.create(title=title)

        return redirect("home")

    todos = Todo.objects.all()
    return render(request, "todo/home.html", {"todos": todos})


def delete_todo(request, id):
    todo = Todo.objects.get(id=id)
    todo.delete()
    return redirect("home")


def complete_todo(request, id):
    todo = Todo.objects.get(id=id)
    todo.completed = not todo.completed
    todo.save()
    return redirect("home")