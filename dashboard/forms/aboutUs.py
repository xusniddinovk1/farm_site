from django import forms
from core.models.aboutUs import *


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['address', 'phone_number', 'email']
        widgets = {
            'address': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Enter address', 'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'placeholder': 'Enter phone number', 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter email', 'class': 'form-control'}),
        }


class AboutUsForm(forms.ModelForm):
    class Meta:
        model = AboutUs
        fields = ['context']
        widgets = {
            'context': forms.Textarea(
                attrs={'rows': 5, 'placeholder': 'Enter about us content', 'class': 'form-control'}),
        }


class FarmHistoryForm(forms.ModelForm):
    class Meta:
        model = FarmHistory
        fields = ['year', 'title', 'slug', 'context']
        widgets = {
            'year': forms.NumberInput(attrs={'placeholder': 'Enter year', 'class': 'form-control'}),
            'title': forms.TextInput(attrs={'placeholder': 'Enter title', 'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'placeholder': 'Enter slug', 'class': 'form-control'}),
            'context': forms.Textarea(
                attrs={'rows': 5, 'placeholder': 'Enter history context', 'class': 'form-control'}),
        }


class OurTeamForm(forms.ModelForm):
    class Meta:
        model = OurTeam
        fields = ['image']
        widgets = {
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }


class PartnerForm(forms.ModelForm):
    class Meta:
        model = Partner
        fields = ['context']
        widgets = {
            'context': forms.Textarea(
                attrs={'rows': 3, 'placeholder': 'Enter partner context', 'class': 'form-control'}),
        }


class PartnerImageForm(forms.ModelForm):
    class Meta:
        model = PartnerImage
        fields = ['partner', 'image']
        widgets = {
            'partner': forms.Select(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }


class ManufacturingForm(forms.ModelForm):
    class Meta:
        model = Manufacturing
        fields = ['title', 'context', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter title', 'class': 'form-control'}),
            'context': forms.Textarea(attrs={'rows': 5, 'placeholder': 'Enter context', 'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
