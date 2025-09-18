// ✅ Roshni Beauty Parlor - Complete JavaScript (Fixed & Safe v7)
(function () {
    const VERSION = "v7";
    console.log(`🚀 Roshni Beauty Parlor JS loaded (${VERSION})`);
  
    document.addEventListener("DOMContentLoaded", function () {
      try {
        initNavbar();
        initAnimations();
        initServices();
        initFormValidation();
        initScrollEffects();
        initTestimonialSlider();
        console.log("✅ All features initialized successfully");
      } catch (error) {
        console.log("⚠️ Initialization error:", error.message);
      }
    });
  
    // ✅ Utility: safe value read
    function val(el) {
      return (el && typeof el.value === "string") ? el.value.trim() : "";
    }
  
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
  
    // ✅ Smooth Scroll + Active Link Highlight
    function initAnimations() {
      try {
        const navLinks = document.querySelectorAll(".navbar-nav a");
        navLinks.forEach((link) => {
          link.addEventListener("click", (e) => {
            const href = link.getAttribute("href");
            if (href && href.startsWith("#")) {
              e.preventDefault();
              const targetId = href.substring(1);
              const targetSection = document.getElementById(targetId);
              if (targetSection) {
                window.scrollTo({
                  top: targetSection.offsetTop - 70,
                  behavior: "smooth",
                });
                navLinks.forEach((l) => l.classList.remove("active"));
                link.classList.add("active");
              }
            }
          });
        });
      } catch (error) {
        console.log("Animations initialization failed:", error.message);
      }
    }
  
    // ✅ Services Card Hover Animation
    function initServices() {
      try {
        const serviceCards = document.querySelectorAll(".service-card");
        serviceCards.forEach((card) => {
          card.addEventListener("mouseenter", () => card.classList.add("hovered"));
          card.addEventListener("mouseleave", () => card.classList.remove("hovered"));
        });
      } catch (error) {
        console.log("Services initialization failed:", error.message);
      }
    }
  
    // ✅ Contact Form Validation (scoped & safe)
    function initFormValidation() {
      try {
        const form = document.getElementById("contactForm"); // only on pages where it exists
        if (!form) {
          console.log("ℹ️ No contact form found on this page");
          return;
        }
  
        // 🔒 Scope queries to THIS form only
        const nameField = form.querySelector("#name");
        const emailField = form.querySelector("#email");
        const messageField = form.querySelector("#message");
  
        form.addEventListener("submit", (e) => {
          e.preventDefault();
  
          // If any field is missing, DON'T touch .value
          if (!nameField || !emailField || !messageField) {
            console.error("⚠️ One or more form fields not found!", {
              hasName: !!nameField,
              hasEmail: !!emailField,
              hasMessage: !!messageField,
            });
            return;
          }
  
          // Safe reads (never touches .value on null)
          const nameVal = val(nameField);
          const emailVal = val(emailField);
          const messageVal = val(messageField);
  
          if (!nameVal) {
            alert("Please enter your name");
            nameField.focus();
            return;
          }
  
          if (!emailVal) {
            alert("Please enter your email");
            emailField.focus();
            return;
          } else if (!emailVal.includes("@")) {
            alert("Please enter a valid email address");
            emailField.focus();
            return;
          }
  
          if (!messageVal) {
            alert("Please enter your message");
            messageField.focus();
            return;
          }
  
          alert("✅ Form submitted successfully!");
          form.reset();
        });
      } catch (error) {
        console.log("Form validation failed:", error.message);
      }
    }
  
    // ✅ Scroll Effects
    function initScrollEffects() {
      try {
        const observerOptions = { threshold: 0.1, rootMargin: "0px 0px -50px 0px" };
        const observer = new IntersectionObserver((entries) => {
          entries.forEach(entry => {
            if (entry.isIntersecting) {
              entry.target.classList.add("animate-in");
            }
          });
        }, observerOptions);
        const animateElements = document.querySelectorAll(".service-card, .testimonial-card, .stat-item");
        animateElements.forEach(el => observer.observe(el));
      } catch (error) {
        console.log("Scroll effects failed:", error.message);
      }
    }
  
    // ✅ Testimonial Slider
    function initTestimonialSlider() {
      try {
        const testimonialCards = document.querySelectorAll(".testimonial-card");
        testimonialCards.forEach((card, index) => {
          card.style.animationDelay = `${index * 0.1}s`;
        });
      } catch (error) {
        console.log("Testimonial slider failed:", error.message);
      }
    }
  
    // ✅ Debounce (utility)
    function debounce(func, wait) {
      let timeout;
      return function executedFunction(...args) {
        const later = () => {
          clearTimeout(timeout);
          func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
      };
    }
  
    // ✅ Global Error Logger
    window.addEventListener("error", function (e) {
      console.log("❌ JavaScript Error:", e.message);
      console.log("📄 File:", e.filename);
      console.log("🔢 Line:", e.lineno);
    });
  })();
  

  