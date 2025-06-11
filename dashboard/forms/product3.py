from django import forms
from core.models.product3 import Aminoacid, Food


class AminoacidForm(forms.ModelForm):
    class Meta:
        model = Aminoacid
        fields = [
            'category', 'for_what', 'animal', 'title', 'slug', 'image',
            'manufacturer', 'effect', 'instruction', 'advantages', 'preparation'
        ]
        widgets = {
            'category': forms.Select(attrs={'class': 'form-control'}),
            'for_what': forms.TextInput(
                attrs={'placeholder': 'Enter what this amino acid is for', 'class': 'form-control'}),
            'animal': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'placeholder': 'Enter title', 'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'placeholder': 'Enter slug', 'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'manufacturer': forms.TextInput(attrs={'placeholder': 'Enter manufacturer', 'class': 'form-control'}),
            'effect': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Enter effect', 'class': 'form-control'}),
            'instruction': forms.Textarea(
                attrs={'rows': 3, 'placeholder': 'Enter instruction', 'class': 'form-control'}),
            'advantages': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Enter advantages', 'class': 'form-control'}),
            'preparation': forms.TextInput(attrs={'placeholder': 'Enter preparation', 'class': 'form-control'}),
        }


class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = [
            'category', 'for_what', 'animal', 'manufacturer', 'title',
            'slug', 'image', 'effect', 'instruction', 'packaging'
        ]
        widgets = {
            'category': forms.Select(attrs={'class': 'form-control'}),
            'for_what': forms.TextInput(attrs={'placeholder': 'Enter what this food is for', 'class': 'form-control'}),
            'animal': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'manufacturer': forms.TextInput(attrs={'placeholder': 'Enter manufacturer', 'class': 'form-control'}),
            'title': forms.TextInput(attrs={'placeholder': 'Enter title', 'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'placeholder': 'Enter slug', 'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'effect': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Enter effect', 'class': 'form-control'}),
            'instruction': forms.Textarea(
                attrs={'rows': 3, 'placeholder': 'Enter instruction', 'class': 'form-control'}),
            'packaging': forms.TextInput(attrs={'placeholder': 'Enter packaging', 'class': 'form-control'}),
        }
