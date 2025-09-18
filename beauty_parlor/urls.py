from django.urls import path
from . import views
from django.contrib.auth import views as auth_views   # ✅ Add this import

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('service/<int:service_id>/', views.service_detail, name='service_detail'),
    path('contact/', views.contact, name='contact'),
    path('booking/', views.booking, name='booking'),
    path('testimonials/', views.testimonials, name='testimonials'),

    # Authentication URLs
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('my-bookings/', views.my_bookings, name='my_bookings'),
    path('booking/<int:booking_id>/', views.booking_detail, name='booking_detail'),
    path('booking/<int:booking_id>/cancel/', views.cancel_booking, name='cancel_booking'),

     # Password Reset URLs
    
    path('password_reset/', 
         auth_views.PasswordResetView.as_view(template_name='auth/password_reset.html'), 
         name='password_reset'),

    path('password_reset/done/', 
         auth_views.PasswordResetDoneView.as_view(template_name='auth/password_reset_done.html'), 
         name='password_reset_done'),

    path('reset/<uidb64>/<token>/', 
         auth_views.PasswordResetConfirmView.as_view(template_name='auth/password_reset_confirm.html'), 
         name='password_reset_confirm'),

    path('reset/done/', 
         auth_views.PasswordResetCompleteView.as_view(template_name='auth/password_reset_complete.html'), 
         name='password_reset_complete'),
    
     path("recommendations/", views.ai_recommendations, name="ai_recommendations"),
    
    
]
