from django.shortcuts import render
from .models import ParkingLot

def index(request):
    return render(request, 'main/index.html')

def list(request):
    list_obj = ParkingLot.objects.all()
    return render(request, 'main/list.html', {'list_obj':list_obj})