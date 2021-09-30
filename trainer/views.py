from.models import Trainer
from django import forms
from django .shortcuts import redirect,render
from django.shortcuts import render
from .forms import TrainerForm

def register_trainer(request):
    if request.method=="POST":
        form=TrainerForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('register_trainer')
        else:
            print(form.errors)
    else:
        form=TrainerForm()
    return render(request,'register_trainer.html',{"form":form}) 

def trainer_list(request):
    trainers=Trainer.objects.all()
    return render(request,"trainer_list.html",{"trainers":trainers})


    
   

    

    
