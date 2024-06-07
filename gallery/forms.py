# gallery/forms.py

from django import forms
from .models import Image

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['image']

#################################
from django import forms
from .models import Image

class MultipleImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('image', 'image2')