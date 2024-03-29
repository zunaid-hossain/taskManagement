from django.shortcuts import render,redirect
from . import forms 
from TaskModel.models import TaskModel
# Create your views here.
def home(request):
    
    data=TaskModel.objects.all()
    return render(request,'model.html',{'data':data})

def add_Task (request):
    if request.method=="POST":
        Task=forms.TaskForm(request.POST)
        if Task.is_valid():
            Task.save()
            return redirect('home')
    else:
        Task=forms.TaskForm()
    
    return render(request,'Add.html',{'form':Task})


def edit_Task (request,id):
    task=TaskModel.objects.get(pk=id)
    Task=forms.TaskForm(instance=task)

    if request.method=="POST":
        Task=forms.TaskForm(request.POST ,instance=task)
        if Task.is_valid():
            Task.save()
            return redirect('home')

    return render(request,'Add.html',{'form':Task})

def delete_Task (request,id):
    task=TaskModel.objects.get(pk=id)
    task.delete()
    return redirect('home')


def done (request,id):
    task=TaskModel.objects.get(pk=id)
    task.is_completed =True
    task.save()
    return redirect('home')


    