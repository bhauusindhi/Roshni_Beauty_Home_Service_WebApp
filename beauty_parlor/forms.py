from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Contact, Booking, Service, UserProfile, Review

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    phone = forms.CharField(max_length=15, required=True)
    address = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}), required=True)
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'phone', 'address', 'password1', 'password2']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['phone', 'address', 'profile_picture', 'date_of_birth']
        widgets = {
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Phone'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Your Address', 'rows': 3}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Phone'}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subject'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Your Message', 'rows': 5}),
        }

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['service', 'date', 'time', 'address', 'special_requests']
        widgets = {
            'service': forms.Select(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Your Address', 'rows': 3}),
            'special_requests': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Any special requests or notes', 'rows': 3}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Only show home services
        self.fields['service'].queryset = Service.objects.filter(is_home_service=True)

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']
        widgets = {
            'rating': forms.Select(choices=[(i, f'{i} Star{"s" if i != 1 else ""}') for i in range(1, 6)], 
            attrs={'class': 'form-control'}),
            'comment': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Share your experience', 'rows': 4}),
        } 