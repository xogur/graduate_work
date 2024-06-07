from django.db import models
from .custom_storage import OverwriteStorage

class Image(models.Model):
    image = models.ImageField(upload_to='images/', storage=OverwriteStorage())
    image2 = models.ImageField(upload_to='images/', storage=OverwriteStorage())  # image2 필드 추가
    uploaded_at = models.DateTimeField(auto_now_add=True)
    image_url = models.URLField(blank=True)

    def __str__(self):
        return self.image.name
    
    class Meta:
        app_label = 'gallery'

class show_Image(models.Model):
    image = models.ImageField(upload_to='media/images/', storage=OverwriteStorage())
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.image.name
    
    class Meta:
        app_label = 'gallery'
