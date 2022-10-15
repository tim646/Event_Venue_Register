from django import forms
from django.forms import ModelForm
from .models import Venue, Event


# VEnue Form

class VenueForm(ModelForm):
    class Meta:
        model = Venue
        fields = ('name', 'address', 'zip_code', 'phone', 'web', 'email',)
        labels = {
            'name': '',
            'address': '',
            'zip_code': '',
            'phone': '',
            'web': '',
            'email': '',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Venue Name'}),
            'address': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Address'}),
            'zip_code': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Zip Code'}),
            'phone': forms.NumberInput(attrs={'class':'form-control', 'placeholder': 'Phone'}),
            'web': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Web link'}),
            'email': forms.EmailInput(attrs={'class':'form-control', 'placeholder': 'Email'}),
        }

# Admin Event Form

class EventFormAdmin(ModelForm):
    class Meta:
        model = Event
        fields = ('name', 'event_date', 'venue', 'manager', 'attendees', 'description',)
        labels = {
            'name': '',
            'event_date': 'YYYY-MM-DD HH:MM:SS',
            'venue': 'Venue',
            'manager': 'Manager',
            'attendees': '',
            'description': '',

        }

        widgets = {

            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Event Name'}),
            'event_date': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Event Date'}),
            'venue': forms.Select(attrs={'class':'form-select', 'placeholder': 'Venue'}),
            'manager': forms.Select(attrs={'class':'form-select', 'placeholder': 'Manager'}),
            'description': forms.Textarea(attrs={'class':'form-control', 'placeholder': 'Description'}),
            'attendees': forms.SelectMultiple(attrs={'class':'form-control', 'placeholder': 'Attendees'}),

        }


# User event form
class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ('name', 'event_date', 'venue', 'attendees', 'description',)
        labels = {
            'name': '',
            'event_date': 'YYYY-MM-DD HH:MM:SS',
            'venue': 'Venue',
            'attendees': '',
            'description': '',

        }

        widgets = {

            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Event Name'}),
            'event_date': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Event Date'}),
            'venue': forms.Select(attrs={'class':'form-select', 'placeholder': 'Venue'}),
            'description': forms.Textarea(attrs={'class':'form-control', 'placeholder': 'Description'}),
            'attendees': forms.SelectMultiple(attrs={'class':'form-control', 'placeholder': 'Attendees'}),

        }

