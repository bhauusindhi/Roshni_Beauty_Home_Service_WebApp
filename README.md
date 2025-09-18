# 🌸 Roshni Beauty Parlor - Home Beauty Services

A comprehensive Django-based web application for a beauty parlor offering professional home beauty services. This application provides a complete booking system, service management, and customer experience platform.

## ✨ Features

### 🎨 **Core Services**

- **Facial Treatments**: Classic, Gold, and Fruit facials
- **Hair Services**: Cut, styling, coloring, and treatments
- **Makeup Services**: Bridal, party, and natural makeup
- **Manicure & Pedicure**: Classic and gel manicures, pedicures
- **Massage Services**: Head, body, and foot massages
- **Waxing Services**: Full body, facial, and leg waxing

### 🚀 **Key Functionality**

- **User Authentication**: Registration, login, and profile management
- **Service Booking**: Easy online booking system with date/time selection
- **Home Service**: All services available at customer's doorstep
- **Testimonials**: Customer reviews and ratings
- **Admin Panel**: Comprehensive service and booking management
- **Responsive Design**: Mobile-friendly interface

### 🛠 **Technical Features**

- **Django 4.2.7**: Modern Python web framework
- **SQLite Database**: Lightweight and efficient
- **Crispy Forms**: Beautiful Bootstrap-styled forms
- **Image Management**: Automatic image downloads for services
- **Responsive CSS**: Modern, mobile-first design
- **JavaScript Enhancements**: Interactive user experience

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- pip (Python package installer)

### Installation

1. **Clone the repository**

   ```bash
   git clone <repository-url>
   cd roshni-beauty-parlor
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run migrations**

   ```bash
   python manage.py migrate
   ```

4. **Create superuser (optional)**

   ```bash
   python manage.py createsuperuser
   ```

5. **Populate with sample data**

   ```bash
   python manage.py populate_data
   ```

6. **Run the development server**

   ```bash
   python manage.py runserver
   ```

7. **Access the application**
   - Main site: http://127.0.0.1:8000/
   - Admin panel: http://127.0.0.1:8000/admin/

## 📁 Project Structure

```
roshni_beauty/
├── beauty_parlor/          # Main application
│   ├── models.py          # Database models
│   ├── views.py           # View functions
│   ├── forms.py           # Form definitions
│   ├── admin.py           # Admin configuration
│   └── urls.py            # URL routing
├── templates/              # HTML templates
│   ├── base.html          # Base template
│   └── beauty_parlor/     # App-specific templates
├── static/                 # Static files
│   ├── css/               # Stylesheets
│   ├── js/                # JavaScript files
│   └── images/            # Static images
├── media/                  # User-uploaded files
│   ├── services/          # Service images
│   ├── testimonials/      # Testimonial images
│   └── profile_pics/      # User profile pictures
└── manage.py              # Django management script
```

## 🎯 Key Models

### Service

- Name, description, price, category
- Duration, home service availability
- High-quality images

### UserProfile

- Extended user information
- Phone, address, profile picture
- Date of birth

### Booking

- Service selection and scheduling
- Address and special requests
- Status tracking (pending, confirmed, completed, cancelled)

### Testimonial

- Customer reviews and ratings
- Service-specific feedback
- Customer images

## 🎨 Customization

### Adding New Services

1. Add service details in `beauty_parlor/management/commands/populate_data.py`
2. Run `python manage.py populate_data` to add to database

### Styling

- Modify `static/css/style.css` for custom styling
- Update color variables in CSS root for brand colors

### JavaScript

- Enhance `static/js/script.js` for additional functionality
- Add form validation and interactive features

## 🔧 Configuration

### Settings

- **DEBUG**: Set to `False` in production
- **SECRET_KEY**: Change in production
- **ALLOWED_HOSTS**: Configure for your domain
- **MEDIA_ROOT**: Configure for file uploads

### Database

- Default: SQLite (development)
- Production: PostgreSQL or MySQL recommended

## 📱 Responsive Design

The application is fully responsive and works on:

- Desktop computers
- Tablets
- Mobile phones
- All modern browsers

## 🚀 Deployment

### Production Checklist

- [ ] Set `DEBUG = False`
- [ ] Configure `ALLOWED_HOSTS`
- [ ] Use production database
- [ ] Configure static file serving
- [ ] Set up media file serving
- [ ] Configure HTTPS
- [ ] Set up backup system

### Recommended Hosting

- **VPS**: DigitalOcean, Linode, AWS
- **Platform**: Heroku, PythonAnywhere
- **Database**: PostgreSQL (production)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👥 Support

For support and questions:

- Email: roshnisindhi20596@gmail.com
- Phone: +91 9426738721
- Location: Vijapur, Gujarat, India

## 🎉 Acknowledgments

- Django community for the excellent framework
- Bootstrap for responsive design components
- Font Awesome for beautiful icons
- Unsplash for high-quality placeholder images

---

**Made with ❤️ for Roshni Beauty Parlor**
