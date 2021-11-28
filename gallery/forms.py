from django import forms
from django.db.models import fields
from .models import Picture

class PictureForm(forms.ModelForm):
    class meta:
        model=Picture
        fields=("image_name", "image")
