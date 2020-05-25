from django.db import models

# Create your models here.
class Image(models.Model):
    image=models.ImageField(blank=True,upload_to='images/')
    image_name=models.CharField(max_length=50)
    image_description=models.TextField()
    date=models.DateTimeField(auto_now_add=True)
    location=models.ForeignKey('Location',on_delete=models.CASCADE)
    category=models.ForeignKey('Category',on_delete=models.CASCADE)
    
    ##Methods
    #SAVE IMAGE
    def save_image(self):
        self.save()
     
    #UPDATE IMAGE
    @classmethod
    def update_image(cls,name,update):
        Image.objects.filter(image_name=name).update(image_name=update)
        update=Image.objects.get(image_name=update)
        return update    
        
    #DELETE IMAGE    
    @classmethod    
    def delete_image(cls,image):
        Image.objects.get(image_name=image).delete()
        
    #GET IMAGE BY ID
    @classmethod
    def get_image_by_id(cls,id):
        image=Image.objects.filter(id=id)
        return image
        
    @classmethod
    def search_image(cls,category_image):
        categories=Category.objects.filter(category=category_image)
        for category in categories:          
            image=cls.objects.filter(category=category)
        return image
        
    @classmethod
    def filter_by_location(cls,image_location):
        locations=Location.objects.filter(location=image_location)
        for location in locations:
            image=Image.objects.filter(location=location)
        return image
    
    def __str__(self):
        return self.image_name
    
class Location(models.Model):
    location=models.CharField(max_length=30)
    
    ##Methods
    #SAVE Location
    def save_location(self):
        self.save()
     
    #UPDATE location
    @classmethod
    def update_location(cls,name,update):
        Location.objects.filter(location=name).update(location=update)  
        updated=Location.objects.get(location=update)
        return updated

        
    #DELETE location    
    @classmethod    
    def delete_location(cls,location):
        deleted=Location.objects.get(location=location).delete()
        return deleted
    
    def __str__(self):
        return self.location
    
CATEGORY=[
        ('Educational','Educational'),
        ('Vacational','Vacational'),
        ('Hobby','Hobby'),
        ('Family','Family'),
        ('Work','Work'),
        ('Fashion','Fashion'),
        ('Sports','Sports'),
]
class Category(models.Model):
    category=models.CharField(max_length=15,choices=CATEGORY)
    
    ##Methods
    #SAVE CATEGORY
    def save_category(self):
        self.save()
     
    #UPDATE CATEGORY
    @classmethod
    def update_category(cls,name,update):
        Category.objects.filter(category=name).update(category=update)
        update=Category.objects.get(category=update)
        return update    
        
    #DELETE IMAGE    
    @classmethod    
    def delete_category(cls,category):
        Category.objects.get(category=category).delete()
    
    def __str__(self):
        return self.category
    