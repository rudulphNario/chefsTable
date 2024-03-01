from django.db import models

# Create your models here.
class Contact(models.Model):
    firstName =  models.CharField(max_length=100)
    lastName = models.CharField(max_length=100,)
    email = models.EmailField()
    phoneNumber = models.CharField(max_length=20)
    message = models.TextField(max_length=1000)
    
    
    def __str__(self):
        return f"{self.firstName} {self.lastName}"