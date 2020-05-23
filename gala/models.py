from django.db import models

# Create your models here.
class Image(models.Model):
    image=models.ImageField(blank=True)
    image_name=models.CharField(max_length=20)
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
        Image.objects.filter(image_name=image).delete()
        
    
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
        deleted=Location.objects.filter(location=location).delete()
        return deleted
    
    def __str__(self):
        return self.location
    
CATEGORY=[
        ('Educational','Educational'),
        ('Vacational','Vacational'),
        ('Hobby','Hobby'),
        ('Family','Family'),
        ('Work','Work'),
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
        update=Category.objects.filter(category=name).update(category=update)
        return update    
        
    #DELETE IMAGE    
    @classmethod    
    def delete_category(cls,category):
        Image.objects.filter(category=category).delete()
    
    def __str__(self):
        return self.category
    