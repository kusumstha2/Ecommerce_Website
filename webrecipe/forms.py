from django.forms import ModelForm
from .models import Product
from django import forms

class CreateForm(ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
        widgets = {
            'product': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Product'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Price'}),
            'category': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Category'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }
