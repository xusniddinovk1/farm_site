from django import forms
from core.models.product2 import Equipment, Paint, Work


class EquipmentForm(forms.ModelForm):
    class Meta:
        model = Equipment
        fields = ['title', 'slug', 'description', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter title', 'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'placeholder': 'Enter slug', 'class': 'form-control'}),
            'description': forms.Textarea(
                attrs={'rows': 4, 'placeholder': 'Enter description', 'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }


class PaintForm(forms.ModelForm):
    class Meta:
        model = Paint
        fields = ['category', 'title', 'slug', 'image', 'dosage', 'animals']
        widgets = {
            'category': forms.Select(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'placeholder': 'Enter title', 'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'placeholder': 'Enter slug', 'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'dosage': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Enter dosage', 'class': 'form-control'}),
            'animals': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }


class WorkForm(forms.ModelForm):
    class Meta:
        model = Work
        fields = ['title', 'slug', 'context', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter title', 'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'placeholder': 'Enter slug', 'class': 'form-control'}),
            'context': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Enter context', 'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
