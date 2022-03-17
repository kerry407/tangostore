from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import TextInput, EmailInput, FileInput, Select
from .models import UserProfile
from django import forms

class UserRegisterForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']
    
    def clean_email(self):
        if self.is_valid():
            email = self.cleaned_data.get('email')
            try:
                account = User.objects.exclude(pk=self.instance.pk).get(email=email)
            except User.DoesNotExist:
                return email 
            raise forms.ValidationError('Email {} is already in use'.format(email))
    
    def clean_username(self):
        if self.is_valid():
            username = self.cleaned_data.get('username')
            try:
                account = User.objects.exclude(pk=self.instance.pk).get(username=username)
            except User.DoesNotExist:
                return username 
            raise forms.ValidationError('Username {} is already in use. Try a different one.'.format(username))




STATE = [
    ('Abuja', 'Abuja'),
    ('Lagos', 'Lagos'),
    ('Ogun', 'Ogun'),
    ('Oyo', 'Oyo'),
]

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile 
        fields = ( 'phone', 'address', 'city', 'state', 'country', 'image')
        widgets = {
            'email': EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}),
            'phone': TextInput(attrs={'class': 'form-control', 'placeholder': 'phone'}),
            'address': TextInput(attrs={'class': 'form-control', 'placeholder':'Address'}),
            'city': TextInput(attrs={'class': 'form-control', 'placeholder': 'city'}),
            'state': Select(attrs={'class': 'form-control', 'placeholder': 'State'}, choices=STATE),
            'country': TextInput(attrs={'class': 'form-control', 'placeholder': 'Country'}),
            'image': FileInput(attrs={'placeholder': 'image'}),
        }

    