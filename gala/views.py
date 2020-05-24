from django.shortcuts import render
from django.http import HttpResponse,Http404
from .models import Image,Location,Category

# Create your views here.
def index(request):
    images=Image.objects.all()
    return render(request,'gala/index.html',{'images':images})

def search_category(request):
    if 'category' in request.GET and request.GET['category']:
        search_term=request.GET.get('category')
        searched_category=Image.objects.filter(category=search_term)
        print(searched_category)
        message=f'{search_term}'
        
        return render(request,'gala/search_category.html',{'message':message,'searched':searched_category,'title':search_term})
    
    else:
        message=f"You haven't searched for anything."
        return render(request,'gala/search_category.html',{'message':message})
    

def search_location(request,location):
    try:
        location=Image.objects.filter(location=location) 
        message=f'{location}' 
        
    except Image.DoesNotExist:
        Http404('Image does not exist')
        
    return render(request,'gala/location.html',{'message':message,'locations':location})

    
