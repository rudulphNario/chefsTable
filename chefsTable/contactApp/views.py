from django.shortcuts import render, redirect
from .form import ContactForm
from .models import  Contact

# Create your views here.

def contact(request):
    return render(request,'contact.html' )

def tableContacting(request):
    contact = Contact.objects.all()
    data = {"contact" : contact}
    return render(request, 'contacting_info.html', data)
def contact_table(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_info')
    else:
        form = ContactForm()
    return render(request, 'contact.html',  {'form': form})