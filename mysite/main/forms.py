from django import forms
from .models import ParkingLot

class ParkingLotForm(forms.ModelForm):
    class Meta:
        model = ParkingLot
        fields = (
            'address',
            'owner',
            'address',
            'time',
            'tel',
            'price',
            'photo',
        )
        