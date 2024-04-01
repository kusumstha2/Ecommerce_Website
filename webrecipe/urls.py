from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('home',home,name="home"),
    path('create',create,name="create"),
    path('view/<id>',view,name="view"),
    path('edit/<id>',edit,name="edit"),
    path('delete/<id>',delete,name="delete"),
    
]
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)