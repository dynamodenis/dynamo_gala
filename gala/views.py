from django.shortcuts import render
from django.http import HttpResponse
from .models import Image,Location,Category

# Create your views here.
def index(request):
    images=Image.objects.all()
    return render(request,'gala/index.html',{'images':images})

def search_category(request):
    if 'category' in request.GET and request.GET['category']:
        search_term=request.GET.get('category')
        searched_category=Image.objects.filter(category=search_term)
        message=f'{search_term}'
        
        return render(request,'gala/search_category.html',{'message':message,'searched':search_category,'title':search_term})
    
    else:
        message=f"You haven't searched for anything."
        return render(request,'gala/search_category.html',{'message':message})