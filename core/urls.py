from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *

urlpatterns = [
    path('register',register,name='register'),
    path('login',login_pg,name='login_pg'),
    path('logout',logout_pg,name='logout'),
]
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
