from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group, User
from django.forms import ModelForm
from .models import *

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

        widgets = {
            'fullname': forms.TextInput(attrs={
                'class': "form-control"
            }),
            'email': forms.EmailInput(attrs={
                'class': "form-control"
            }),
            'message': forms.Textarea(attrs={
                'class': "form-control"
            }),
            'phonenumber': forms.TextInput(attrs={
                'class': "form-control"
            }),
            'organization': forms.TextInput(attrs={
                'class': "form-control"
            }),
        }

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ('title', 'content', 'rating')
        widgets = {
            'title': forms.TextInput(attrs={
                'class': "form-control",
                'placeholder': "Title"
            }),
            'content': forms.Textarea(attrs={
                'class': "form-control",
                'rows': '3',
                'placeholder': "How was our service?"
            }),
            'rating': forms.Select(attrs={
                'class': "form-control",
            }),
        }

class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = ('pickup', 'dropoff', 'driver')
        widgets = {
            'pickup': forms.TextInput(attrs={
                'class': "form-control",
                'placeholder': "Pickup Location"
            }),
            'dropoff': forms.TextInput(attrs={
                'class': "form-control",
                'placeholder': "Drop-off Location"
            }),
        }
