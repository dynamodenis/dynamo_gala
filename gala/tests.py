from django.test import TestCase
from .models import Location,Image,Category

# Create your tests here.
#TESTS IMAGE MODEL
class TestImage(TestCase):
    def setUp(self):
        self.location1=Location(location='Donholm')
        self.location1.save_location()
        self.category1=Category(category='Work')
        self.category1.save_category()
        self.image1=Image(image_name='This is a Test',image_description='test image',location=self.location1,category=self.category1)
        self.image1.save_image()
     
     #obects saved test   
    def test_save_image(self):
        self.category1.save_category()
        self.location1.save_location()
        self.image1.save_image()
        
    #objects updated
    def test_updated_image(self):
        update=Image.update_image(self.image1.image_name,'Updated Test')
        self.assertEqual(update.image_name,'Updated Test')
     
     # DELETE IMAGE   
    def test_delete_image(self):
        Image.delete_image(self.image1.image_name)
        self.assertTrue(len(Image.objects.all())==0)
        
    #GET IMAGE BY ID
    def test_get_image_by_id(self):
        image=Image.get_image_by_id(self.image1.id)
        self.assertTrue(len(image)==1)
        
    #SEARCH IMAGE BY CATEGORY
    def test_search_image(self):
        image=Image.search_image(self.image1.category.category)
        self.assertTrue(len(image)>0)
    
    #FILTER BY LOCATION
    def test_filter_by_location(self):
        image=Image.filter_by_location(self.image1.location)
        self.assertTrue(len(image)>0)
        
    
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
        update=Location.update_location(self.location.location,'Umoja')
        self.assertEqual(update.location,'Umoja')
        
    def test_delete_location(self):
        delete=Location.delete_location(self.location)
        self.assertTrue(len(Location.objects.all())==0)
        
        
        
        
#TEST CATEGORY MODEL
class TestCategory(TestCase):
    def setUp(self):
        self.category=Category(category='Hobby')
        self.category.save()
        
        
    def test_category_saved(self):
        self.category.save_category()
        
    def test_update_category(self):
        update=Category.update_category(self.category.category,'Work')
        self.assertEqual(update.category,'Work')
        
    def test_delete_category(self):
        Category.delete_category(self.category.category)
        self.assertTrue(len(Category.objects.all())==0)