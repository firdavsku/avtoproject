from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from .models import Car, Category

class CarView(ListView):
    model = Car
    template_name = 'index.html'
    context_object_name = 'Car'


def car_detail(request,id):    
    cars=Car.objects.get(id=id)
    cars.save()
    print(cars)
    return render(request,'batafsil.html',{"cars":cars})