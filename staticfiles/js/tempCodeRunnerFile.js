// ✅ Roshni Beauty Parlor - Main JavaScript File
// Handles all interactive features and form validation

// Wait for DOM to be fully loaded
document.addEventListener("DOMContentLoaded", function () {
    try {
        // Initialize all features
        initNavbar();
        initAnimations();
        initServices();
        initFormValidation();
        initScrollEffects();
        initTestimonialSlider();
        
        console.log("✅ All features initialized successfully");
    } catch (error) {
        console.log("⚠️ Some features may not be available on this page:", error.message);
    }
});

// ✅ Mobile Navigation Toggle
function initNavbar() {
    try {
        const navToggle = document.querySelector(".navbar-toggler");
        const navMenu = document.querySelector(".navbar-collapse");
        
        if (navToggle && navMenu) {
            navToggle.addEventListener("click", () => {
                navMenu.classList.toggle("show");
                navToggle.classList.toggle("collapsed");
            });
        }
    } catch (error) {
        console.log("Navbar initialization failed:", error.message);
    }
}

// ✅ Smooth Scrolling for Navigation Links
function initScrollEffects() {
    try {
        const navLinks = document.querySelectorAll('a[href^="#"]');
        
        navLinks.forEach(link => {
            if (link && link.addEventListener) {
                link.addEventListener("click", function (e) {
                    e.preventDefault();
                    
                    const targetId = this.getAttribute("href");
                    const targetSection = document.querySelector(targetId);
                    
                    if (targetSection) {
                        targetSection.scrollIntoView({
                            behavior: "smooth",
                            block: "start"
                        });
                    }
                });
            }
        });
    } catch (error) {
        console.log("Scroll effects initialization failed:", error.message);
    }
}

// ✅ Animated Elements on Scroll
function initAnimations() {
    try {
        const animatedElements = document.querySelectorAll(".animate-on-scroll");
        
        if (animatedElements && animatedElements.length > 0) {
            const observer = new IntersectionObserver((entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        entry.target.classList.add("animated");
                    }
                });
            });
            
            animatedElements.forEach(el => {
                if (el) observer.observe(el);
            });
        }
    } catch (error) {
        console.log("Animation initialization failed:", error.message);
    }
}

// ✅ Services Card Hover Effects
function initServices() {
    try {
        const serviceCards = document.querySelectorAll(".service-card");
        
        if (serviceCards && serviceCards.length > 0) {
            serviceCards.forEach(card => {
                if (card && card.addEventListener && card.classList) {
                    card.addEventListener("mouseenter", () => {
                        card.classList.add("hovered");
                    });
                    
                    card.addEventListener("mouseleave", () => {
                        card.classList.remove("hovered");
                    });
                }
            });
        }
    } catch (error) {
        console.log("Services initialization failed:", error.message);
    }
}

// ✅ Testimonial Slider (if multiple testimonials)
function initTestimonialSlider() {
    try {
        const testimonials = document.querySelectorAll(".testimonial-card");
        
        if (testimonials && testimonials.length > 3) {
            // Add slider functionality for many testimonials
            let currentIndex = 0;
            
            function showTestimonials() {
                testimonials.forEach((testimonial, index) => {
                    if (index >= currentIndex && index < currentIndex + 3) {
                        testimonial.style.display = "block";
                    } else {
                        testimonial.style.display = "none";
                    }
                });
            }
            
            // Show first 3 testimonials initially
            showTestimonials();
        }
    } catch (error) {
        console.log("Testimonial slider initialization failed:", error.message);
    }
}

// ✅ Contact Form Validation
function initFormValidation() {
    try {
        const forms = document.querySelectorAll("form");
        
        forms.forEach(form => {
            if (form && form.addEventListener) {
                form.addEventListener("submit", function (e) {
                    e.preventDefault();
                    
                    // Get form elements with multiple fallback strategies
                    let nameField = null;
                    let emailField = null;
                    let messageField = null;
                    let phoneField = null;
                    
                    // Try to find name field
                    nameField = this.querySelector("#name") || 
                               this.querySelector('input[name="name"]') ||
                               this.querySelector('input[placeholder*="name" i]') ||
                               this.querySelector('input[placeholder*="Name" i]');
                    
                    // Try to find email field
                    emailField = this.querySelector("#email") || 
                                this.querySelector('input[name="email"]') ||
                                this.querySelector('input[type="email"]') ||
                                this.querySelector('input[placeholder*="email" i]') ||
                                this.querySelector('input[placeholder*="Email" i]');
                    
                    // Try to find message field
                    messageField = this.querySelector("#message") || 
                                  this.querySelector('textarea[name="message"]') ||
                                  this.querySelector('textarea[placeholder*="message" i]') ||
                                  this.querySelector('textarea[placeholder*="Message" i]');
                    
                    // Try to find phone field
                    phoneField = this.querySelector("#phone") || 
                                this.querySelector('input[name="phone"]') ||
                                this.querySelector('input[type="tel"]') ||
                                this.querySelector('input[placeholder*="phone" i]') ||
                                this.querySelector('input[placeholder*="Phone" i]');
                    
                    // Validate only if the fields exist and have values
                    let hasErrors = false;
                    
                    if (nameField) {
                        if (!nameField.value || !nameField.value.trim()) {
                            showError("Please enter your name", nameField);
                            hasErrors = true;
                        } else {
                            removeError(nameField);
                        }
                    }
                    
                    if (emailField && !hasErrors) {
                        if (!emailField.value || !emailField.value.trim()) {
                            showError("Please enter your email", emailField);
                            hasErrors = true;
                        } else if (!isValidEmail(emailField.value)) {
                            showError("Please enter a valid email address", emailField);
                            hasErrors = true;
                        } else {
                            removeError(emailField);
                        }
                    }
                    
                    if (phoneField && !hasErrors) {
                        if (phoneField.value && !isValidPhone(phoneField.value)) {
                            showError("Please enter a valid phone number", phoneField);
                            hasErrors = true;
                        } else {
                            removeError(phoneField);
                        }
                    }
                    
                    if (messageField && !hasErrors) {
                        if (!messageField.value || !messageField.value.trim()) {
                            showError("Please enter your message", messageField);
                            hasErrors = true;
                        } else {
                            removeError(messageField);
                        }
                    }
                    
                    // If no errors, submit the form
                    if (!hasErrors) {
                        showSuccess("Form submitted successfully! We'll get back to you soon. ✅");
                        this.reset();
                        
                        // Remove any error styling
                        this.querySelectorAll('.is-invalid').forEach(field => {
                            field.classList.remove('is-invalid');
                        });
                    }
                });
            }
        });
    } catch (error) {
        console.log("Form validation initialization failed:", error.message);
    }
}

// ✅ Helper Functions for Form Validation
function isValidEmail(email) {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
}

function isValidPhone(phone) {
    const phoneRegex = /^[\+]?[1-9][\d]{0,15}$/;
    return phoneRegex.test(phone.replace(/[\s\-\(\)]/g, ''));
}

function showError(message, field) {
    // Remove existing error
    removeError(field);
    
    // Add error styling
    field.classList.add('is-invalid');
    
    // Create error message element
    const errorDiv = document.createElement('div');
    errorDiv.className = 'invalid-feedback';
    errorDiv.textContent = message;
    
    // Insert error message after the field
    field.parentNode.appendChild(errorDiv);
    
    // Focus on the field
    field.focus();
}

function removeError(field) {
    field.classList.remove('is-invalid');
    
    // Remove error message
    const errorDiv = field.parentNode.querySelector('.invalid-feedback');
    if (errorDiv) {
        errorDiv.remove();
    }
}

function showSuccess(message) {
    // Create success alert
    const successAlert = document.createElement('div');
    successAlert.className = 'alert alert-success alert-dismissible fade show';
    successAlert.innerHTML = `
        ${message}
        <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
    `;
    
    // Insert at the top of the form
    const form = document.querySelector('form');
    if (form) {
        form.parentNode.insertBefore(successAlert, form);
        
        // Auto-remove after 5 seconds
        setTimeout(() => {
            if (successAlert.parentNode) {
                successAlert.remove();
            }
        }, 5000);
    }
}

// ✅ Price Calculator for Services (if needed)
function calculatePrice(serviceId, duration) {
    try {
        const serviceElement = document.querySelector(`[data-service-id="${serviceId}"]`);
        if (serviceElement) {
            const basePrice = parseFloat(serviceElement.dataset.basePrice) || 0;
            const hourlyRate = parseFloat(serviceElement.dataset.hourlyRate) || 0;
            
            if (duration && hourlyRate) {
                const totalPrice = basePrice + (duration * hourlyRate);
                return totalPrice.toFixed(2);
            }
            
            return basePrice.toFixed(2);
        }
    } catch (error) {
        console.log("Price calculation failed:", error.message);
        return "0.00";
    }
}

// ✅ Lazy Loading for Images
function initLazyLoading() {
    try {
        const images = document.querySelectorAll('img[data-src]');
        
        if (images && images.length > 0) {
            const imageObserver = new IntersectionObserver((entries, observer) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        const img = entry.target;
                        img.src = img.dataset.src;
                        img.classList.remove('lazy');
                        imageObserver.unobserve(img);
                    }
                });
            });
            
            images.forEach(img => {
                if (img) imageObserver.observe(img);
            });
        }
    } catch (error) {
        console.log("Lazy loading initialization failed:", error.message);
    }
}

// ✅ Initialize lazy loading
document.addEventListener("DOMContentLoaded", initLazyLoading);

console.log("🚀 Roshni Beauty Parlor JavaScript loaded successfully!");
