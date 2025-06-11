from django import forms
from core.models.misc import *


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['title', 'slug']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter category title', 'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'placeholder': 'Enter slug', 'class': 'form-control'}),
        }


class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter animal name', 'class': 'form-control'}),
        }


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['title', 'slug', 'context', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter service title', 'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'placeholder': 'Enter slug', 'class': 'form-control'}),
            'context': forms.Textarea(attrs={'rows': 5, 'placeholder': 'Enter context', 'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'slug', 'content', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter news title', 'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'placeholder': 'Enter slug', 'class': 'form-control'}),
            'content': forms.Textarea(attrs={'rows': 5, 'placeholder': 'Enter content', 'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }


class GalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = ['image']
        widgets = {
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
