from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Service, Testimonial, Contact, Booking, UserProfile, Review
from .forms import ContactForm, BookingForm, UserRegistrationForm, UserProfileForm, ReviewForm

def home(request):
    services = Service.objects.filter(is_home_service=True)[:6]
    testimonials = Testimonial.objects.all()[:3]
    context = {
        'services': services,
        'testimonials': testimonials,
    }
    return render(request, 'beauty_parlor/home.html', context)

def about(request):
    return render(request, 'beauty_parlor/about.html')

def services(request):
    category = request.GET.get('category', '')
    search_query = request.GET.get('search', '')
    
    services = Service.objects.all()
    
    if category:
        services = services.filter(category=category)
    
    if search_query:
        services = services.filter(
            Q(name__icontains=search_query) | 
            Q(description__icontains=search_query)
        )
    
    paginator = Paginator(services.order_by('name'), 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'category': category,
        'search_query': search_query,
    }
    return render(request, 'beauty_parlor/services.html', context)

def service_detail(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    related_services = Service.objects.filter(category=service.category).exclude(id=service_id)[:3]
    
    context = {
        'service': service,
        'related_services': related_services,
    }
    return render(request, 'beauty_parlor/service_detail.html', context)

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('contact')
    else:
        form = ContactForm()
    
    context = {
        'form': form,
    }
    return render(request, 'beauty_parlor/contact.html', context)

@login_required
def booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user  # Always set the user for new bookings
            booking.save()
            messages.success(request, f'Booking request submitted successfully! Booking ID: {booking.id}')
            return redirect('my_bookings')
    else:
        form = BookingForm()
    
    services = Service.objects.filter(is_home_service=True)
    context = {
        'form': form,
        'services': services,
    }
    return render(request, 'beauty_parlor/booking.html', context)

def testimonials(request):
    testimonials = Testimonial.objects.all()
    context = {
        'testimonials': testimonials,
    }
    return render(request, 'beauty_parlor/testimonials.html', context)

# Authentication Views
def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            
            # Create user profile
            UserProfile.objects.create(
                user=user,
                phone=form.cleaned_data['phone'],
                address=form.cleaned_data['address']
            )
            
            # Auto login after registration
            login(request, user)
            messages.success(request, 'Registration successful! Welcome to Roshni Beauty Parlor.')
            return redirect('home')
    else:
        form = UserRegistrationForm()
    
    context = {
        'form': form,
    }
    return render(request, 'beauty_parlor/register.html', context)

def user_login(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome back, {user.first_name}!')
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')
    
    return render(request, 'beauty_parlor/login.html')

def user_logout(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('home')

@login_required
def profile(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('profile')
    else:
        form = UserProfileForm(instance=user_profile)
    
    context = {
        'form': form,
        'user_profile': user_profile,
    }
    return render(request, 'beauty_parlor/profile.html', context)

@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user).order_by('-created_at')
    context = {
        'bookings': bookings,
    }
    return render(request, 'beauty_parlor/my_bookings.html', context)

@login_required
def booking_detail(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.booking = booking
            review.save()
            messages.success(request, 'Review submitted successfully!')
            return redirect('my_bookings')
    else:
        form = ReviewForm()
    
    context = {
        'booking': booking,
        'form': form,
    }
    return render(request, 'beauty_parlor/booking_detail.html', context)

@login_required
def cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    
    if booking.status == 'pending':
        booking.status = 'cancelled'
        booking.save()
        messages.success(request, 'Booking cancelled successfully!')
    else:
        messages.error(request, 'This booking cannot be cancelled.')
    
    return redirect('my_bookings') 

def ai_recommendations(request):
    category = request.GET.get("category", "")
    search_query = request.GET.get("search", "")

    # Basic recommendation logic (you can make smarter later)
    recommended = Service.objects.all()
    if category:
        recommended = recommended.filter(category__icontains=category)
    if search_query:
        recommended = recommended.filter(
            Q(name__icontains=search_query) | Q(description__icontains=search_query)
        )

    context = {
        "recommended": recommended[:9],  # limit results
        "category": category,
        "search_query": search_query,
    }
    return render(request, "beauty_parlor/recommendations.html", context)
