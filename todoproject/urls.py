from django.contrib import admin
from django.urls import path
from todo import views

urlpatterns = [
    path("admin/", admin.site.urls),

    path("", views.home, name="home"),

    path("login/", views.user_login, name="login"),

    path("register/", views.register, name="register"),

    path("logout/", views.user_logout, name="logout"),

    path("delete/<int:id>/", views.delete_todo, name="delete"),

    path("complete/<int:id>/", views.complete_todo, name="complete"),
]