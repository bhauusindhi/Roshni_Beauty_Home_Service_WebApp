from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    phone = models.CharField(max_length=15, blank=True)
    address = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.user.username}'s Profile"

class Service(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='services/', blank=True, null=True)
    category = models.CharField(max_length=100, choices=[
        ('facial', 'Facial'),
        ('hair', 'Hair'),
        ('makeup', 'Makeup'),
        ('manicure', 'Manicure & Pedicure'),
        ('massage', 'Massage'),
        ('waxing', 'Waxing'),
    ])
    is_home_service = models.BooleanField(default=False)
    duration = models.IntegerField(help_text='Duration in minutes', default=60)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']

class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    service = models.CharField(max_length=100)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    comment = models.TextField()
    image = models.ImageField(upload_to='testimonials/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name} - {self.service}"

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name} - {self.subject}"

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings', null=True, blank=True)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    address = models.TextField()
    is_home_service = models.BooleanField(default=True)
    status = models.CharField(max_length=20, choices=[
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ], default='pending')
    special_requests = models.TextField(blank=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.user.username if self.user else 'Anonymous'} - {self.service.name} - {self.date}"
    
    def save(self, *args, **kwargs):
        if not self.total_amount:
            self.total_amount = self.service.price
        super().save(*args, **kwargs)

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    booking = models.OneToOneField(Booking, on_delete=models.CASCADE, related_name='review')
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.booking.service.name}" 