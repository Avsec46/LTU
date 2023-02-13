from django.shortcuts import render
from . models import *

# Create your views here.


def home(request):
    return render(request, 'pages/home/home.html')



def about(request):
    data={
        'aboutData':AboutUs.objects.all()
    }
    return render('')


