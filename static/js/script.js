document.addEventListener('DOMContentLoaded', function () {
    initNavbar();
    initAnimations();
    initFormValidation();
    initSmoothScrolling();
    initTestimonialsSlider();
    initServiceFilter();
    initBookingForm();
    initContactForm();
    initScrollEffects();
    initMobileMenu();
    initLazyLoading();
});

// Navbar functionality
function initNavbar() {
    const navbar = document.querySelector('.navbar');
    const navbarToggler = document.querySelector('.navbar-toggler');
    const navbarCollapse = document.querySelector('.navbar-collapse');

    if (!navbar) return;

    // Navbar scroll effect
    window.addEventListener('scroll', function () {
        if (window.scrollY > 50) {
            navbar.classList.add('navbar-scrolled');
        } else {
            navbar.classList.remove('navbar-scrolled');
        }
    });

    // Mobile menu close on link click
    if (navbarCollapse && navbarToggler) {
        const navLinks = document.querySelectorAll('.navbar-nav .nav-link');
        navLinks.forEach(link => {
            link.addEventListener('click', function () {
                if (navbarCollapse.classList.contains('show')) {
                    navbarToggler.click();
                }
            });
        });
    }
}

// Animations on scroll
function initAnimations() {
    const animateElements = document.querySelectorAll('.card, .stat-item, .service-card, .testimonial-card');
    if (!animateElements.length) return;

    const observer = new IntersectionObserver(entries => {
        entries.forEach(entry => {
            if (entry.isIntersecting) entry.target.classList.add('animate-in');
        });
    }, { threshold: 0.1, rootMargin: '0px 0px -50px 0px' });

    animateElements.forEach(el => observer.observe(el));
}

// Form validation
function initFormValidation() {
    const forms = document.querySelectorAll('form');
    if (!forms.length) return;

    forms.forEach(form => {
        form.addEventListener('submit', function (e) {
            if (!validateForm(form)) e.preventDefault();
        });
    });
}

function validateForm(form) {
    let isValid = true;
    const inputs = form.querySelectorAll('input, textarea, select');

    inputs.forEach(input => {
        if (input.hasAttribute('required') && !input.value.trim()) {
            showFieldError(input, 'This field is required');
            isValid = false;
        } else if (input.type === 'email' && input.value && !isValidEmail(input.value)) {
            showFieldError(input, 'Please enter a valid email address');
            isValid = false;
        } else if (input.type === 'tel' && input.value && !isValidPhone(input.value)) {
            showFieldError(input, 'Please enter a valid phone number');
            isValid = false;
        } else {
            clearFieldError(input);
        }
    });

    return isValid;
}

function showFieldError(input, message) {
    clearFieldError(input);
    input.classList.add('is-invalid');

    const errorDiv = document.createElement('div');
    errorDiv.className = 'invalid-feedback';
    errorDiv.textContent = message;
    input.parentNode.appendChild(errorDiv);
}

function clearFieldError(input) {
    input.classList.remove('is-invalid');
    const errorDiv = input.parentNode.querySelector('.invalid-feedback');
    if (errorDiv) errorDiv.remove();
}

const isValidEmail = email => /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
const isValidPhone = phone => /^[\+]?[1-9][\d]{0,15}$/.test(phone.replace(/\s/g, ''));

// Smooth scrolling
function initSmoothScrolling() {
    const links = document.querySelectorAll('a[href^="#"]');
    if (!links.length) return;

    links.forEach(link => {
        link.addEventListener('click', function (e) {
            e.preventDefault();
            const targetElement = document.querySelector(this.getAttribute('href'));
            if (targetElement) targetElement.scrollIntoView({ behavior: 'smooth', block: 'start' });
        });
    });
}

// Testimonials slider
function initTestimonialsSlider() {
    const testimonials = document.querySelectorAll('.testimonial-card');
    if (testimonials.length <= 1) return;

    let currentIndex = 0;
    setInterval(() => {
        testimonials[currentIndex].style.opacity = '0.5';
        currentIndex = (currentIndex + 1) % testimonials.length;
        testimonials[currentIndex].style.opacity = '1';
    }, 5000);
}

// Service filter
function initServiceFilter() {
    const filterButtons = document.querySelectorAll('.service-filter-btn');
    const serviceCards = document.querySelectorAll('.service-card');
    if (!filterButtons.length || !serviceCards.length) return;

    filterButtons.forEach(button => {
        button.addEventListener('click', function () {
            const category = this.getAttribute('data-category');

            filterButtons.forEach(btn => btn.classList.remove('active'));
            this.classList.add('active');

            serviceCards.forEach(card => {
                const cardCategory = card.getAttribute('data-category');
                card.style.display = (category === 'all' || cardCategory === category) ? 'block' : 'none';
            });
        });
    });
}

// Booking form enhancements
function initBookingForm() {
    const bookingForm = document.querySelector('#booking-form');
    if (!bookingForm) return;

    const serviceSelect = bookingForm.querySelector('#id_service');
    const dateInput = bookingForm.querySelector('#id_date');
    const timeInput = bookingForm.querySelector('#id_time');

    if (dateInput) {
        const today = new Date().toISOString().split('T')[0];
        dateInput.setAttribute('min', today);
    }

    if (timeInput) {
        timeInput.addEventListener('change', function () {
            const hour = parseInt(this.value.split(':')[0], 10);
            if (hour < 9 || hour > 20) {
                showFieldError(this, 'Please select a time between 9:00 AM and 8:00 PM');
            } else {
                clearFieldError(this);
            }
        });
    }

    if (serviceSelect) {
        serviceSelect.addEventListener('change', function () {
            const price = this.options[this.selectedIndex].getAttribute('data-price');
            const priceDisplay = document.querySelector('.service-price');
            if (priceDisplay && price) {
                priceDisplay.textContent = `₹${price}`;
                priceDisplay.style.display = 'block';
            }
        });
    }
}

// Contact form enhancements
function initContactForm() {
    const contactForm = document.querySelector('#contact-form');
    if (!contactForm) return;

    const messageTextarea = contactForm.querySelector('#id_message');
    if (messageTextarea) {
        messageTextarea.addEventListener('input', function () {
            const maxLength = 1000;
            const currentLength = this.value.length;
            const remaining = maxLength - currentLength;

            let counter = contactForm.querySelector('.char-counter');
            if (!counter) {
                counter = document.createElement('small');
                counter.className = 'char-counter text-muted';
                messageTextarea.parentNode.appendChild(counter);
            }

            counter.textContent = `${remaining} characters remaining`;
            counter.classList.toggle('text-danger', currentLength > maxLength);
        });
    }
}

// Scroll effects
function initScrollEffects() {
    const parallaxElements = document.querySelectorAll('.parallax');
    if (!parallaxElements.length) return;

    window.addEventListener('scroll', function () {
        const scrolled = window.pageYOffset;
        parallaxElements.forEach(element => {
            const speed = element.getAttribute('data-speed') || 0.5;
            element.style.transform = `translateY(${-(scrolled * speed)}px)`;
        });
    });
}

// Mobile menu
function initMobileMenu() {
    const navbarToggler = document.querySelector('.navbar-toggler');
    const navbarCollapse = document.querySelector('.navbar-collapse');
    if (!navbarToggler || !navbarCollapse) return;

    navbarToggler.addEventListener('click', () => {
        navbarCollapse.classList.toggle('show');
    });

    document.addEventListener('click', e => {
        if (!navbarToggler.contains(e.target) && !navbarCollapse.contains(e.target)) {
            navbarCollapse.classList.remove('show');
        }
    });
}

// Lazy loading for images
function initLazyLoading() {
    const images = document.querySelectorAll('img[data-src]');
    if (!images.length) return;

    const imageObserver = new IntersectionObserver(entries => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const img = entry.target;
                img.src = img.dataset.src;
                img.classList.remove('lazy');
                imageObserver.unobserve(img);
            }
        });
    });

    images.forEach(img => imageObserver.observe(img));
}

// Performance optimization
window.addEventListener('load', function () {
    document.querySelectorAll('.loading').forEach(loader => loader.style.display = 'none');
    document.querySelectorAll('.content-hidden').forEach(item => item.classList.remove('content-hidden'));
});

// Inject CSS for animations
const style = document.createElement('style');
style.textContent = `
    .animate-in { animation: fadeInUp 0.6s ease forwards; }
    @keyframes fadeInUp { from {opacity:0;transform:translateY(30px);} to {opacity:1;transform:translateY(0);} }
    .navbar-scrolled { background: rgba(44, 62, 80, 0.95) !important; backdrop-filter: blur(10px); }
    .content-hidden { opacity: 0; }
    .service-filter-btn.active { background-color: var(--primary-color); color: white; }
    .char-counter { font-size: 0.875rem; margin-top: 0.25rem; }
`;
document.head.appendChild(style);