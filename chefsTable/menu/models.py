from django.db import models

# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField(null=False)
    menu_item_description =  models.TextField(max_length= 1000, default= '')
    
    def __str__(self):
        return self.name
class TableBooking(models.Model):
    firstName = models.CharField(max_length=100)
    lastName =  models.CharField(max_length=100)
    phoneNumber = models.CharField(max_length=10)
    guestNumber = models.IntegerField()
    day = models.DateField()
    time = models.TimeField(auto_now_add=True)
    table_number = models.IntegerField(unique=True)
    
    def __str__(self):
        return  f"{self.firstName}  {self.lastName}"

    