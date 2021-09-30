from django.shortcuts import render
from.forms import CoursesRegistrationForms
from.models import Courses


def register_courses(request):
    if request.method=="POST":
        form= CoursesRegistrationForms(request.POST)
        if form.is_valid():
              form.save()
        else:
            print(form.errors)  
    else:
        form=CoursesRegistrationForms()          
    return render(request,"register_courses.html",{"form":form})
def courses_list(request):
    courses=Courses.objects.all()
    return render(request,"course_list.html",{"courses":courses})

# Create your views here.
