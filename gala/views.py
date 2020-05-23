from django.shortcuts import render
from django.http import HttpResponse
from .models import Image,Location,Category

# Create your views here.
def index(request):
    images=Image.objects.all()
    return render(request,'gala/index.html',{'images':images})