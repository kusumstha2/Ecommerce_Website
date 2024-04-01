from django.urls import path
from .views import *

urlpatterns = [
    path('register',register,name='register'),
    path('login',login_pg,name='login_pg'),
]
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
