from django.core.management.base import BaseCommand
from django.core.files import File
from beauty_parlor.models import Service, Testimonial
from decimal import Decimal
import requests
import os
from django.conf import settings

class Command(BaseCommand):
    help = 'Populate database with sample beauty services and testimonials with images'

    def download_image(self, url, filename, folder):
        """Download image from URL and save to media folder"""
        try:
            self.stdout.write(f'  - Attempting to download: {url}')
            
            response = requests.get(url, timeout=30, headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
            })
            response.raise_for_status()
            
            # Create folder if it doesn't exist
            folder_path = os.path.join(settings.MEDIA_ROOT, folder)
            os.makedirs(folder_path, exist_ok=True)
            
            # Save image
            file_path = os.path.join(folder_path, filename)
            with open(file_path, 'wb') as f:
                f.write(response.content)
            
            self.stdout.write(f'  - Successfully downloaded: {filename}')
            return file_path
        except Exception as e:
            self.stdout.write(
                self.style.WARNING(f'Failed to download image {url}: {str(e)}')
            )
            return None

    def handle(self, *args, **options):
        self.stdout.write('Creating sample beauty services...')
        
        # Clear existing services first
        Service.objects.all().delete()
        self.stdout.write('  - Cleared existing services')
        
        # Sample services data with beauty-specific image URLs
        services_data = [
            # Facial Services
            {
                'name': 'Classic Facial',
                'description': 'Deep cleansing facial with natural ingredients. Includes cleansing, exfoliation, mask, and moisturizing. Perfect for all skin types.',
                'price': Decimal('800.00'),
                'category': 'facial',
                'is_home_service': True,
                'duration': 60,
                'image_url': 'https://images.unsplash.com/photo-1570172619644-dfd03ed5d881?w=400&h=300&fit=crop&crop=face'
            },
            {
                'name': 'Gold Facial',
                'description': 'Luxury gold facial for radiant skin. Includes gold particles for anti-aging benefits and skin rejuvenation.',
                'price': Decimal('1500.00'),
                'category': 'facial',
                'is_home_service': True,
                'duration': 90,
                'image_url': 'https://images.unsplash.com/photo-1556228720-195a672e8a03?w=400&h=300&fit=crop'
            },
            {
                'name': 'Fruit Facial',
                'description': 'Natural fruit-based facial for glowing skin. Rich in vitamins and antioxidants for healthy skin.',
                'price': Decimal('1000.00'),
                'category': 'facial',
                'is_home_service': True,
                'duration': 75,
                'image_url': 'https://images.unsplash.com/photo-1556228720-195a672e8a03?w=400&h=300&fit=crop&crop=face'
            },
            
            # Hair Services
            {
                'name': 'Hair Cut & Style',
                'description': 'Professional haircut and styling service. Includes consultation and styling tips for your face shape.',
                'price': Decimal('600.00'),
                'category': 'hair',
                'is_home_service': True,
                'duration': 45,
                'image_url': 'https://images.unsplash.com/photo-1562322140-8baeececf3df?w=400&h=300&fit=crop'
            },
            {
                'name': 'Hair Color',
                'description': 'Professional hair coloring service with premium products. Includes consultation and color matching.',
                'price': Decimal('1200.00'),
                'category': 'hair',
                'is_home_service': True,
                'duration': 120,
                'image_url': 'https://images.unsplash.com/photo-1605497788044-5a32c7078486?w=400&h=300&fit=crop'
            },
            {
                'name': 'Hair Treatment',
                'description': 'Deep conditioning hair treatment for damaged hair. Restores moisture and shine to your locks.',
                'price': Decimal('800.00'),
                'category': 'hair',
                'is_home_service': True,
                'duration': 60,
                'image_url': 'https://images.unsplash.com/photo-1522337360788-8b13dee7a37e?w=400&h=300&fit=crop'
            },
            
            # Makeup Services
            {
                'name': 'Bridal Makeup',
                'description': 'Complete bridal makeup package. Includes trial, touch-up kit, and hair styling for your special day.',
                'price': Decimal('5000.00'),
                'category': 'makeup',
                'is_home_service': True,
                'duration': 180,
                'image_url': 'https://images.unsplash.com/photo-1596462502278-27bfdc403348?w=400&h=300&fit=crop'
            },
            {
                'name': 'Party Makeup',
                'description': 'Glamorous party makeup with long-lasting products. Perfect for special occasions and events.',
                'price': Decimal('1500.00'),
                'category': 'makeup',
                'is_home_service': True,
                'duration': 90,
                'image_url': 'https://images.unsplash.com/photo-1594736797933-d0401ba2fe65?w=400&h=300&fit=crop'
            },
            {
                'name': 'Natural Makeup',
                'description': 'Light and natural makeup for everyday look. Enhances natural beauty without being heavy.',
                'price': Decimal('800.00'),
                'category': 'makeup',
                'is_home_service': True,
                'duration': 60,
                'image_url': 'https://images.unsplash.com/photo-1594736797933-d0401ba2fe65?w=400&h=300&fit=crop&crop=face'
            },
            
            # Manicure & Pedicure
            {
                'name': 'Classic Manicure',
                'description': 'Basic manicure service. Includes nail shaping, cuticle care, and polish application.',
                'price': Decimal('400.00'),
                'category': 'manicure',
                'is_home_service': True,
                'duration': 45,
                'image_url': 'https://images.unsplash.com/photo-1604654894610-df63bc536371?w=400&h=300&fit=crop'
            },
            {
                'name': 'Gel Manicure',
                'description': 'Long-lasting gel manicure. Chip-resistant and glossy finish that lasts for weeks.',
                'price': Decimal('800.00'),
                'category': 'manicure',
                'is_home_service': True,
                'duration': 60,
                'image_url': 'https://images.unsplash.com/photo-1604654894610-df63bc536371?w=400&h=300&fit=crop'
            },
            {
                'name': 'Pedicure',
                'description': 'Relaxing pedicure service. Includes foot soak, exfoliation, and polish for beautiful feet.',
                'price': Decimal('600.00'),
                'category': 'manicure',
                'is_home_service': True,
                'duration': 60,
                'image_url': 'https://images.unsplash.com/photo-1604654894610-df63bc536371?w=400&h=300&fit=crop'
            },
            
            # Massage Services
            {
                'name': 'Head Massage',
                'description': 'Therapeutic head massage for stress relief. Promotes hair growth and relaxation.',
                'price': Decimal('500.00'),
                'category': 'massage',
                'is_home_service': True,
                'duration': 45,
                'image_url': 'https://images.unsplash.com/photo-1544161512-6ad79e18fd98?w=400&h=300&fit=crop'
            },
            {
                'name': 'Body Massage',
                'description': 'Full body massage for complete relaxation. Uses premium oils and therapeutic techniques.',
                'price': Decimal('1200.00'),
                'category': 'massage',
                'is_home_service': True,
                'duration': 90,
                'image_url': 'https://images.unsplash.com/photo-1544161512-6ad79e18fd98?w=400&h=300&fit=crop'
            },
            {
                'name': 'Foot Massage',
                'description': 'Reflexology foot massage. Relieves tension and promotes circulation in your feet.',
                'price': Decimal('400.00'),
                'category': 'massage',
                'is_home_service': True,
                'duration': 30,
                'image_url': 'https://images.unsplash.com/photo-1544161512-6ad79e18fd98?w=400&h=300&fit=crop'
            },
            
            # Waxing Services
            {
                'name': 'Full Body Waxing',
                'description': 'Complete body waxing service. Includes all areas with premium wax for smooth skin.',
                'price': Decimal('2000.00'),
                'category': 'waxing',
                'is_home_service': True,
                'duration': 120,
                'image_url': 'https://images.unsplash.com/photo-1556228720-195a672e8a03?w=400&h=300&fit=crop'
            },
            {
                'name': 'Facial Waxing',
                'description': 'Eyebrow and upper lip waxing. Precise shaping and grooming for perfect brows.',
                'price': Decimal('300.00'),
                'category': 'waxing',
                'is_home_service': True,
                'duration': 30,
                'image_url': 'https://images.unsplash.com/photo-1556228720-195a672e8a03?w=400&h=300&fit=crop&crop=face'
            },
            {
                'name': 'Leg Waxing',
                'description': 'Full leg waxing service. Smooth and long-lasting results for beautiful legs.',
                'price': Decimal('800.00'),
                'category': 'waxing',
                'is_home_service': True,
                'duration': 60,
                'image_url': 'https://images.unsplash.com/photo-1556228720-195a672e8a03?w=400&h=300&fit=crop'
            },
            
            # Additional Beauty Services
            {
                'name': 'Threading',
                'description': 'Traditional hair removal technique using cotton thread. Perfect for eyebrows and facial hair.',
                'price': Decimal('200.00'),
                'category': 'threading',
                'is_home_service': True,
                'duration': 20,
                'image_url': 'https://images.unsplash.com/photo-1556228720-195a672e8a03?w=400&h=300&fit=crop&crop=face'
            },
            {
                'name': 'Henna Art',
                'description': 'Beautiful henna designs for hands and feet. Perfect for special occasions and festivals.',
                'price': Decimal('500.00'),
                'category': 'henna',
                'is_home_service': True,
                'duration': 60,
                'image_url': 'https://images.unsplash.com/photo-1604654894610-df63bc536371?w=400&h=300&fit=crop'
            },
            {
                'name': 'Skin Treatment',
                'description': 'Advanced skin treatments for acne, pigmentation, and anti-aging. Uses medical-grade products.',
                'price': Decimal('2500.00'),
                'category': 'skin',
                'is_home_service': True,
                'duration': 120,
                'image_url': 'https://images.unsplash.com/photo-1570172619644-dfd03ed5d881?w=400&h=300&fit=crop&crop=face'
            }
        ]
        
        # Create services
        for service_data in services_data:
            image_url = service_data.pop('image_url', None)
            
            service, created = Service.objects.get_or_create(
                name=service_data['name'],
                defaults=service_data
            )
            
            if created:
                self.stdout.write(f'Created service: {service.name}')
                
                # Download and assign image
                if image_url:
                    filename = f"{service.name.lower().replace(' ', '_').replace('&', 'and')}.jpg"
                    image_path = self.download_image(image_url, filename, 'services')
                    if image_path:
                        try:
                            with open(image_path, 'rb') as img_file:
                                service.image.save(filename, File(img_file), save=True)
                                self.stdout.write(f'  - Successfully assigned image: {filename}')
                        except Exception as e:
                            self.stdout.write(
                                self.style.ERROR(f'Failed to assign image {filename}: {str(e)}')
                            )
        
        self.stdout.write('Creating sample testimonials...')
        
        # Clear existing testimonials first
        Testimonial.objects.all().delete()
        self.stdout.write('  - Cleared existing testimonials')
        
        # Sample testimonials data with beauty-specific image URLs
        testimonials_data = [
            {
                'name': 'Priya Sharma',
                'service': 'Bridal Makeup',
                'rating': 5,
                'comment': 'Amazing bridal makeup service! The team was professional and made me look stunning on my special day. The makeup stayed perfect throughout the ceremony and reception. Highly recommended!',
                'image_url': 'https://images.unsplash.com/photo-1494790108755-2616b612b786?w=200&h=200&fit=crop&crop=face'
            },
            {
                'name': 'Meera Patel',
                'service': 'Gold Facial',
                'rating': 5,
                'comment': 'The gold facial was absolutely luxurious! My skin feels so smooth and radiant. The therapist was very skilled and used premium products. Will definitely book again!',
                'image_url': 'https://images.unsplash.com/photo-1438761681033-6461ffad8d80?w=200&h=200&fit=crop&crop=face'
            },
            {
                'name': 'Anjali Desai',
                'service': 'Hair Treatment',
                'rating': 4,
                'comment': 'Great hair treatment service. My hair feels so much healthier and softer. The home service was very convenient and the stylist was professional.',
                'image_url': 'https://images.unsplash.com/photo-1544005313-94ddf0286df2?w=200&h=200&fit=crop&crop=face'
            },
            {
                'name': 'Riya Gupta',
                'service': 'Party Makeup',
                'rating': 5,
                'comment': 'Perfect party makeup! The makeup stayed flawless throughout the evening. Very professional service and beautiful results. Everyone complimented my look!',
                'image_url': 'https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=200&h=200&fit=crop&crop=face'
            },
            {
                'name': 'Sneha Reddy',
                'service': 'Body Massage',
                'rating': 5,
                'comment': 'Relaxing body massage at home. The therapist was skilled and used excellent techniques. I felt completely rejuvenated after the session. Highly satisfied!',
                'image_url': 'https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=200&h=200&fit=crop&crop=face'
            },
            {
                'name': 'Kavya Singh',
                'service': 'Gel Manicure',
                'rating': 4,
                'comment': 'Beautiful gel manicure that lasted for weeks! The nail art was perfect and the service was excellent. The technician was very careful and precise.',
                'image_url': 'https://images.unsplash.com/photo-1494790108755-2616b612b786?w=200&h=200&fit=crop&crop=face'
            }
        ]
        
        # Create testimonials
        for testimonial_data in testimonials_data:
            image_url = testimonial_data.pop('image_url', None)
            
            testimonial, created = Testimonial.objects.get_or_create(
                name=testimonial_data['name'],
                service=testimonial_data['service'],
                defaults=testimonial_data
            )
            
            if created:
                self.stdout.write(f'Created testimonial: {testimonial.name}')
                
                # Download and assign image
                if image_url:
                    filename = f"{testimonial.name.lower().replace(' ', '_')}.jpg"
                    image_path = self.download_image(image_url, filename, 'testimonials')
                    if image_path:
                        try:
                            with open(image_path, 'rb') as img_file:
                                testimonial.image.save(filename, File(img_file), save=True)
                                self.stdout.write(f'  - Successfully assigned image: {filename}')
                        except Exception as e:
                            self.stdout.write(
                                self.style.ERROR(f'Failed to assign image {filename}: {str(e)}')
                            )
        
        self.stdout.write(
            self.style.SUCCESS('Successfully populated database with sample beauty services and testimonials with images!')
        ) 