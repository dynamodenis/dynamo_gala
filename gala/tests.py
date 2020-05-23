from django.test import TestCase
from .models import Location,Image,Category

# Create your tests here.
#TESTS IMAGE MODEL
class TestImage(TestCase):
    def setUp(self):
        self.location1=Location(location='Donholm')
        self.category1=Category(category='Work')
        self.image1=Image(image_name='This is a Test',image_description='test image',location=self.location1,category=self.category1)
     
     #obects saved test   
    def test_save_image(self):
        self.category1.save_category()
        self.location1.save_location()
        self.image1.save_image()
        
    #objects updated
    
#TEST LOCATION MODEL       
class TestLocation(TestCase):
    def setUp(self):
        self.location=Location(location='Donholm')
        self.location.save_location()
    
    def tearDown(self):
        Location.objects.all().delete()
            
    def test_location_save(self):
        self.location.save_location()
        
    def test_update_location(self):
        update=Location.update_location('Donholm','Umoja')
        self.assertEqual(update.location,'Umoja')
        
    def test_delete_location(self):
        delete=Location.delete_location(self.location)
        self.assertTrue(len(Location.objects.all())==0)
        
        
        
        
#TEST CATEGORY MODEL
class TestCategory(TestCase):
    def setUp(self):
        self.category=Category(category='Hobby')
        
        
    def test_category_saved(self):
        self.category.save_category()