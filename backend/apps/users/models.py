# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.postgres.fields import ArrayField
from apps.trips.models import TravelStyle





class User(AbstractUser):
    email = models.EmailField(unique=True)
    is_verified = models.BooleanField(default=False)
    birth_date = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profiles/', null=True, blank=True)
    location = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=100, blank=True)
    region = models.CharField(max_length=100, blank=True)
    postal_code = models.CharField(max_length=20, blank=True)
    country = models.CharField(max_length=100, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    social_links = ArrayField(models.URLField(), default=list, blank=True)

    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)




class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

    travel_styles = ArrayField(models.CharField(max_length=50, choices=TravelStyle.choices), default=list)
    budget_range = models.CharField(max_length=20, choices=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High')])
    travel_frequency = models.CharField(max_length=20, choices=[
        ('rarely', 'Rarely'), ('occasionally', 'Occasionally'), ('frequently', 'Frequently')
    ])
    preferred_transport = ArrayField(models.CharField(max_length=30), default=list, blank=True)
    favorite_activities = ArrayField(models.CharField(max_length=50), default=list, blank=True)

    preferred_gender_match = models.CharField(max_length=20, choices=[
        ('any', 'Any'), ('male', 'Male'), ('female', 'Female'), ('nonbinary', 'Non-binary')
    ], default='any')
    age_range_min = models.IntegerField(default=18)
    age_range_max = models.IntegerField(default=99)

    languages_spoken = ArrayField(models.CharField(max_length=30), default=list, blank=True)
    remote_worker = models.BooleanField(default=False)
    open_to_romance = models.BooleanField(default=False)
    open_to_friendship = models.BooleanField(default=True)




