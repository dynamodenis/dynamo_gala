from django.shortcuts import render
from django.http import HttpResponse,Http404
from .models import Image,Location,Category

# Create your views here.
def index(request):
    images=Image.objects.all()
    return render(request,'gala/index.html',{'images':images})

def get_image_by_id(request,image_id):
    images=Image.get_image_by_id(image_id)
    return render(request,'gala/index.html', {'images':images})
     

def search_category(request):
    if 'category' in request.GET and request.GET['category']:
        search_term=request.GET.get('category')
        searched_category=Image.search_image(search_term)
        print(searched_category)
        message=f'{search_term}'
        
        return render(request,'gala/search_category.html',{'message':message,'searched':searched_category,'title':search_term})
    
    else:
        message=f"You haven't searched for anything."
        return render(request,'gala/search_category.html',{'message':message})
    

def filter_by_location(request,location_id):
    try:
        get_location_id=Location.objects.get(pk=location_id)
        location=Image.filter_by_location(get_location_id) 
        message=f'{get_location_id}' 
        
    except Image.DoesNotExist:
        Http404('Image does not exist')
        
    return render(request,'gala/location.html',{'message':message,'locations':location})


def get_image_id(request,image_id):
    try:
        image=Image.get_image_by_id(image_id)
        message=f'{image.image_name}'
    except Image.DoesNotExist:
        Http404('Image Does Not Exist')
    
    return render(request, 'gala/image.html',{'image':image,'message':message,'title':image.image_name})
    
