from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact

# Create your views here.

def index(request):
    context={
        'variable' : 'this is the value'
    }
    return render(request, 'index.html', context)
    # return HttpResponse("this is the homepage")

def about(request):
    return render(request, 'about.html')
    # return HttpResponse("This is about page")

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, 
        date=datetime.today())
        contact.save()
    return render(request, 'contact.html')
    # return HttpResponse("This is the contact page")

def services(request):
    return render(request, 'services.html')
    # return HttpResponse("This is the service page")