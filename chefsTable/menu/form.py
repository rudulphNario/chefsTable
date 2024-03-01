from django import forms
from .models import TableBooking

# class BookingForm(forms.Form):
#     firstName = forms.CharField(max_length=100)
#     lastName = forms.CharField(max_length=100)
#     phoneNumber = forms.CharField(max_length=10)
#     guestNumber = forms.IntegerField()
#     day = forms.DateTimeField()
#     time = forms.TimeField(auto_now_add=True)
#     table_number =  forms.IntegerField(unique=True)
    
class BookingForm(forms.ModelForm):
    class Meta:  #inheret the object in model 
        model = TableBooking
        fields = "__all__"
    