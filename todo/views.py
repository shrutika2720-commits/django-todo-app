from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from .models import Todo


# HOME / TODO APP
def home(request):

    if not request.user.is_authenticated:
        return redirect("login")

    if request.method == "POST":

        title = request.POST.get("title")

        if title:
            Todo.objects.create(
                user=request.user,
                title=title
            )

        return redirect("home")

    # ONLY LOGGED-IN USER'S TASKS
    todos = Todo.objects.filter(
        user=request.user
    )

    return render(
        request,
        "todo/home.html",
        {
            "todos": todos
        }
    )


# DELETE TODO
def delete_todo(request, id):

    todo = Todo.objects.get(
        id=id,
        user=request.user
    )

    todo.delete()

    return redirect("home")


# COMPLETE TODO
def complete_todo(request, id):

    todo = Todo.objects.get(
        id=id,
        user=request.user
    )

    todo.completed = not todo.completed

    todo.save()

    return redirect("home")


# REGISTER
def register(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        if password != confirm_password:

            return render(
                request,
                "todo/register.html",
                {
                    "error": "Passwords do not match."
                }
            )

        if User.objects.filter(
            username=username
        ).exists():

            return render(
                request,
                "todo/register.html",
                {
                    "error": "Username already exists."
                }
            )

        if username and password:

            user = User.objects.create_user(
                username=username,
                password=password
            )

            login(request, user)

            return redirect("home")

    return render(
        request,
        "todo/register.html"
    )


# LOGIN
def user_login(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            return redirect("home")

        return render(
            request,
            "todo/login.html",
            {
                "error": "Invalid username or password."
            }
        )

    return render(
        request,
        "todo/login.html"
    )


# LOGOUT
def user_logout(request):

    logout(request)

    return redirect("login")