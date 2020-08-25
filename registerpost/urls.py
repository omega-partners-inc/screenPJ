from django.contrib import admin
from django.urls import path
from .views import registerview

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', registerview,name='register'),
]