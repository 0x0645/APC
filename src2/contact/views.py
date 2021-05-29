from django.shortcuts import render
from .models import Contact
from django.http import HttpResponse
# from django.contrib import messages
# Create your views here.





def Contact(request):
    if request.method=='Post':
        contact = Contact()
        name = request.Post.get('name')
        email = request.Post.get('email')
        phone_number = request.Post.get('phone')
        message = request.Post.get('Message')
        contact.name=name
        contact.name=email
        contact.name=phone_number
        contact.name=message
        contact.save()
        # messages.success(request, 'Message Created Succesfully.')
        return HttpResponse("<h2>Thanks For Contact Us</h2>")

    return render(request , 'contact/contact.html')