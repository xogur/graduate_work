# gallery/urls.py

from django.urls import path
from . import views

app_name = 'gallery'

urlpatterns = [
    path('', views.upload_image, name='upload_image'),
    path('images/', views.show_images, name='show_images'),
    path('processing/', views.processing_page, name='processing_page'),
]
