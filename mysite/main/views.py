from django.shortcuts import render
from .models import ParkingLot
from .forms import ParkingLotForm

def index(request):
    return render(request, 'main/index.html')

def parkinglist(request):    
    pLotList_obj = ParkingLot.objects.all()
    
    if request.method == "POST":
        form = ParkingLotForm(request.POST, request.FILES)
        print(request)
        print(dir(request.POST))
        # keys = list(request.POST.keys())
        keys = list(request.POST.items())
        
        print(keys)
        
        if form.is_valid():
            parkingLot = form.save(commit=False)
            parkingLot.save()
            pLotList_obj = ParkingLot.objects.all()
            return render(request, 'main/parkinglist.html', {'pLotList_obj':pLotList_obj})
        else:
            form = ParkingLotForm()
            return render(request, 'main/add.html')
            
    
    return render(request, 'main/parkinglist.html', {'pLotList_obj':pLotList_obj})

def detail(request, pk):    
    pLot_obj = ParkingLot.objects.get(pk=pk)
    return render(request, 'main/detail.html', {'pLot_obj':pLot_obj})

def detail_test(request):
    return render(request, 'main/detail.html')

def layout(request):
    return render(request, 'main/layout.html')

def add(request):
    return render(request, 'main/add.html')

def edit(request):
    return render(request, 'main/edit.html')

def apply(request):
    return render(request, 'main/apply.html')

def mypage(request):
    return render(request, 'main/mypage.html')
