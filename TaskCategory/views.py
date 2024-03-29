from django.shortcuts import render,redirect
from . import forms 
from TaskModel.models import TaskCategory

# Create your views here.
def home(request):
    return render(request,'category.html')


def add_category (request):
    if request.method=="POST":
        categor=forms.Category(request.POST)
        if categor.is_valid():
            categor.save()
            return redirect('Home_M')
    else:
        categor=forms.Category()
    
    return render(request,'Add.html',{'form':categor})


