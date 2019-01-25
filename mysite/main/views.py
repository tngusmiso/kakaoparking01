from django.shortcuts import render
from .models import ParkingLot


def index(request):
    return render(request, 'main/index.html')

def parking_list(request): 
    pLotList_obj = ParkingLot.objects.all()
    return render(request, 'main/list.html', {'pLotList_obj': pLotList_obj})


def detail(request, pk): 
    pLot_obj = ParkingLot.objects.get(pk=pk)
    return render(request, 'main/detail.html', {'pLot_obj':pLot_obj})


def layout(request):
    return render(request, 'main/layout.html')

def add(request):
    return render(request, 'main/add.html')

def edit(request):
    return render(request, 'main/edit.html')

def apply(request):
    return render(request, 'main/apply.html')
