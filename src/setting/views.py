from django.shortcuts import render
from souq.models import Souq
from products.models import category

# Create your views here.




def Home(request):
    da=Souq.objects.all()
    Categories = category.objects.all().order_by('sweetName')

    return render(request,'setting/home.html',{'Categories':Categories})







