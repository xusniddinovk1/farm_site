from django import forms
from core.models.product1 import CleaningProducts, VitaminsMinerals


class CleaningProductsForm(forms.ModelForm):
    class Meta:
        model = CleaningProducts
        fields = [
            'category', 'for_what', 'animal', 'manufacturer',
            'title', 'slug', 'image', 'about', 'structure',
            'usage', 'packaging'
        ]
        widgets = {
            'category': forms.Select(attrs={'class': 'form-control'}),
            'for_what': forms.TextInput(
                attrs={'placeholder': 'Enter what this product is for', 'class': 'form-control'}),
            'animal': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'manufacturer': forms.TextInput(attrs={'placeholder': 'Enter manufacturer', 'class': 'form-control'}),
            'title': forms.TextInput(attrs={'placeholder': 'Enter title', 'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'placeholder': 'Enter slug', 'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'about': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Enter about', 'class': 'form-control'}),
            'structure': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Enter structure', 'class': 'form-control'}),
            'usage': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Enter usage', 'class': 'form-control'}),
            'packaging': forms.TextInput(attrs={'placeholder': 'Enter packaging', 'class': 'form-control'}),
        }


class VitaminsMineralsForm(forms.ModelForm):
    class Meta:
        model = VitaminsMinerals
        fields = [
            'category', 'for_what', 'animal', 'title', 'slug',
            'image', 'effect', 'dosage', 'contraindications',
            'instruction', 'packaging'
        ]
        widgets = {
            'category': forms.Select(attrs={'class': 'form-control'}),
            'for_what': forms.TextInput(attrs={'placeholder': 'Enter what this is for', 'class': 'form-control'}),
            'animal': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'placeholder': 'Enter title', 'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'placeholder': 'Enter slug', 'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'effect': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Enter effect', 'class': 'form-control'}),
            'dosage': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Enter dosage', 'class': 'form-control'}),
            'contraindications': forms.Textarea(
                attrs={'rows': 3, 'placeholder': 'Enter contraindications', 'class': 'form-control'}),
            'instruction': forms.Textarea(
                attrs={'rows': 3, 'placeholder': 'Enter instruction', 'class': 'form-control'}),
            'packaging': forms.TextInput(attrs={'placeholder': 'Enter packaging', 'class': 'form-control'}),
        }
