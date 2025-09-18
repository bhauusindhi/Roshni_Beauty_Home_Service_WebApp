from django.contrib import admin
from .models import Service, Testimonial, Contact, Booking, UserProfile, Review

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'phone', 'created_at']
    list_filter = ['created_at']
    search_fields = ['user__username', 'user__first_name', 'user__last_name', 'phone']
    readonly_fields = ['created_at', 'updated_at']

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'duration', 'is_home_service', 'created_at']
    list_filter = ['category', 'is_home_service', 'created_at']
    search_fields = ['name', 'description']
    list_editable = ['price', 'duration', 'is_home_service']

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['name', 'service', 'rating', 'created_at']
    list_filter = ['rating', 'created_at']
    search_fields = ['name', 'service', 'comment']

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'created_at']
    list_filter = ['created_at']
    search_fields = ['name', 'email', 'subject', 'message']
    readonly_fields = ['created_at']

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['user', 'service', 'date', 'time', 'status', 'total_amount', 'created_at']
    list_filter = ['status', 'date', 'created_at', 'is_home_service']
    search_fields = ['user__username', 'user__first_name', 'user__last_name', 'service__name']
    list_editable = ['status']
    readonly_fields = ['created_at', 'updated_at', 'total_amount']
    date_hierarchy = 'created_at'

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['user', 'booking', 'rating', 'created_at']
    list_filter = ['rating', 'created_at']
    search_fields = ['user__username', 'booking__service__name', 'comment']
    readonly_fields = ['created_at'] 