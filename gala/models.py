from django.db import models

# Create your models here.
class Image(models.Model):
    image=models.ImageField(blank=True)
    image_name=models.CharField(max_length=20)
    image_description=models.TextField()
    date=models.DateTimeField(auto_now_add=True)
    location=models.ForeignKey('Location',on_delete=models.CASCADE)
    category=models.ForeignKey('Category',on_delete=models.CASCADE)
    
    def __str__(self):
        return self.image_name
    
class Location(models.Model):
    location=models.CharField(max_length=30)
    
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
    
    def __str__(self):
        return self.category
    