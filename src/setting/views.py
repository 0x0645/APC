from django.shortcuts import render
from souq.models import Souq
from products.models import category
from .models import Info
from django.core.mail import send_mail
from django.conf import settings



# Create your views here.






def Home(request):
    da=Souq.objects.filter(manufacture="apple")[:10]
    
    Categories = category.objects.all().order_by('sweetName')

    return render(request,'setting/home.html',{'Categories':Categories,"featured":da})






def contact(request):
    info =Info.objects.last()
    Categories = category.objects.all().order_by('sweetName')
    if request.method=='POST':
        Name=request.POST['name']
        Email=request.POST['email']
        Subject=request.POST['subject']
        Message=request.POST['message']
        send_mail(
            Subject,
            f'Message From : {Name} \n Email : {Email} \n Message : {Message}',
            Email,
            [settings.EMAIL_HOST_USER],
            fail_silently=False,
            )

    return render(request,'setting/contact.html',{
        'info':info,
        'Categories':Categories
        })


