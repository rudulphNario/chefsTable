from django.shortcuts import render, redirect
from .models import Menu, TableBooking
from .form import BookingForm


# Create your views here.
def  home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html' )


def blog(request):
    return render(request,'blog.html' )
def menu(request):
    menu_data = Menu.objects.all()
    main_data = {"menu": menu_data}
    return render(request, 'menu.html',main_data)

def tableBooking(request):
    bookings = TableBooking.objects.all()
    data = {"bookings" : bookings}
    return render(request, 'booking.html', data)

def book_table(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('booking')
    else:
        form = BookingForm()
    return render(request, 'book.html',  {'form': form})