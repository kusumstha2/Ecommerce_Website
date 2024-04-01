from django.forms import ModelForm
from .models import *
from django import forms 

class CreateForm(ModelForm):
    class Meta:
        model=Recipe
        fields="__all__"
        widgets={
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Recipe Name'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'}),
            'ingredient': forms.Textarea(attrs={'class': 'form-control','placeholder': 'Ingredients'}),
            'instruction': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Instruction'}),
            'category': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Category'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'user': forms.HiddenInput(),
        } 