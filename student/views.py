from django.shortcuts import redirect,render
from .models import Student
from .forms import StudentRegistrationForms
from django import forms

def register_student(request):
    if request.method=="POST":
        form=StudentRegistrationForms(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('register_student')
        else:
            print(form.errors)
    else:
        form=StudentRegistrationForms()
    return render(request,"register_student.html",{"form":form})

def student_list(request):
    students=Student.objects.all()
    return render(request,"student_list.html",{"students":students})


def student_profile(request,id):
    student=Student.objects.get(id=id)
    return render(request,"student_profile.html",{"student":student})


def edit_student(request,id):
    student=Student.object.get(id=id)
    if request.method =="POST":
        form=StudentRegistrationForms(request.post,instance=student)
        if form.is_valid():
            form.save()
    else:
        form=StudentRegistrationForms(instance=student)
        return render(request,"edit_student",{"form":form})

def delete_student(request,id):
    student=Student.objects.get(id=id)
    student.delete()
    return redirect(student_list)


