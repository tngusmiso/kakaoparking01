from django.db import models

class ParkingLot(models.Model):
    owner = models.CharField(max_length = 10)
    address = models.CharField(max_length = 50)
    tel = models.IntegerField()
    price = models.IntegerField()
    distance = models.IntegerField()
    photo = models.ImageField()
    
    def __str__(self):
        return self.address