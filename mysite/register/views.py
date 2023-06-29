from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm, RegisterstudentForm
from school.models import Student
from django.contrib.auth.models import User

# Create your views here.
def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
        return redirect("/student/")
    else:
        form = RegisterForm()
    return render(response, "register/register.html",{"form":form})

def registerstudent(response):
    if response.method == "POST":
        form = RegisterstudentForm(response.POST)
        if form.is_valid():
            a = form.cleaned_data["name"]
            b = form.cleaned_data["surname"]
            c = Student.objects.count() + 1
            t = Student(user=response.user, name=a, surname=b, index=c)
            t.save()
            return redirect('/student/')
    else:
        form = RegisterstudentForm()

    return render(response, "register/registerstudent.html",{"form":form})
