from django import forms
from core.models.product import VeterinaryDrugs, Vaccine


class VeterinaryDrugsForm(forms.ModelForm):
    class Meta:
        model = VeterinaryDrugs
        fields = [
            'category', 'for_what', 'animals', 'title', 'slug',
            'image', 'structure', 'instruction', 'dosage',
            'release_period', 'manufacturer'
        ]
        widgets = {
            'category': forms.Select(attrs={'class': 'form-control'}),
            'for_what': forms.TextInput(attrs={'placeholder': 'Enter what this drug is for', 'class': 'form-control'}),
            'animals': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'placeholder': 'Enter title', 'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'placeholder': 'Enter slug', 'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'structure': forms.TextInput(attrs={'placeholder': 'Enter structure', 'class': 'form-control'}),
            'instruction': forms.Textarea(
                attrs={'rows': 4, 'placeholder': 'Enter instruction', 'class': 'form-control'}),
            'dosage': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Enter dosage', 'class': 'form-control'}),
            'release_period': forms.TextInput(attrs={'placeholder': 'Enter release period', 'class': 'form-control'}),
            'manufacturer': forms.TextInput(attrs={'placeholder': 'Enter manufacturer', 'class': 'form-control'}),
        }


class VaccineForm(forms.ModelForm):
    class Meta:
        model = Vaccine
        fields = [
            'category', 'title', 'slug', 'for_what', 'structure',
            'animals', 'image', 'manufacturer', 'drug', 'usage',
            'expiration_date', 'storage'
        ]
        widgets = {
            'category': forms.Select(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'placeholder': 'Enter title', 'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'placeholder': 'Enter slug', 'class': 'form-control'}),
            'for_what': forms.TextInput(
                attrs={'placeholder': 'Enter what this vaccine is for', 'class': 'form-control'}),
            'structure': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Enter structure', 'class': 'form-control'}),
            'animals': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'manufacturer': forms.TextInput(attrs={'placeholder': 'Enter manufacturer', 'class': 'form-control'}),
            'drug': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Enter drug information', 'class': 'form-control'}),
            'usage': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Enter usage', 'class': 'form-control'}),
            'expiration_date': forms.Textarea(
                attrs={'rows': 2, 'placeholder': 'Enter expiration date', 'class': 'form-control'}),
            'storage': forms.Textarea(
                attrs={'rows': 3, 'placeholder': 'Enter storage instructions', 'class': 'form-control'}),
        }
