from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views
app_name='gala'
urlpatterns = [
    path('', views.index, name='index'),
    path('search/',views.search_category,name='search_category'),
    path('<str:location>/',views.filter_by_location,name='filter_by_location')
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
