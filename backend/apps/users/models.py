from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.core.exceptions import ValidationError


class TravelPriority(models.Model):
    code = models.CharField(max_length=20, unique=True)
    label = models.CharField(max_length=100)

    def __str__(self):
        return self.label

class BudgetRange(models.Model):
    code = models.CharField(max_length=20, unique=True)
    label = models.CharField(max_length=100)

    def __str__(self):
        return self.code

class TravelStyle(models.Model):
    code = models.CharField(max_length=20, unique=True)
    label = models.CharField(max_length=100)

    def __str__(self):
        return self.code

class TravelFrequency(models.Model):
    code = models.CharField(max_length=20, unique=True)
    label = models.CharField(max_length=100)

    def __str__(self):
        return self.code

class PrefTransport(models.Model):
    code = models.CharField(max_length=20, unique=True)
    label = models.CharField(max_length=100)

    def __str__(self):
        return self.code

class PrefGenderMatch(models.Model):
    code = models.CharField(max_length=20, unique=True)
    label = models.CharField(max_length=100)

    def __str__(self):
        return self.code

class TravelWith(models.Model):
    code = models.CharField(max_length=20, unique=True)
    label = models.CharField(max_length=100)

    def __str__(self):
        return self.code

class TravelPersona(models.Model):
    code = models.CharField(max_length=20, unique=True)
    label = models.CharField(max_length=100)

    def __str__(self):
        return self.code


class User(AbstractUser):
    # Przenosimy większość danych do UserProfile dla przejrzystości
    email = models.EmailField(unique=True)
    is_verified = models.BooleanField(default=False)

    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username

class Activity(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Language(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name

class DreamDestination(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class LuggageStyle(models.Model):
    code = models.CharField(max_length=30, unique=True)
    label = models.CharField(max_length=100)

    def __str__(self):
        return self.label


class AccommodationPreference(models.Model):
    code = models.CharField(max_length=30, unique=True)
    label = models.CharField(max_length=100)

    def __str__(self):
        return self.label


class PhotoSharingPreference(models.Model):
    code = models.CharField(max_length=30, unique=True)
    label = models.CharField(max_length=100)

    def __str__(self):
        return self.label



class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

    birth_date = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profiles/', null=True, blank=True)
    location = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=100, blank=True)
    region = models.CharField(max_length=100, blank=True)
    postal_code = models.CharField(max_length=20, blank=True)
    country = models.CharField(max_length=100, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    social_links = ArrayField(models.URLField(), default=list, blank=True)

    # Travel preferences
    travel_styles = models.ForeignKey(TravelStyle, null=True, blank=True, on_delete=models.SET_NULL)
    budget_range = models.ForeignKey(BudgetRange, null=True, blank=True, on_delete=models.SET_NULL)
    custom_budget = models.IntegerField(null=True, blank=True)
    travel_frequency = models.ForeignKey(TravelFrequency, null=True, blank=True, on_delete=models.SET_NULL)
    custom_travel_schedule = models.TextField(blank=True, null=True)
    remote_worker = models.BooleanField(default=False)
    preferred_transport = models.ForeignKey(PrefTransport,null=True, blank=True, on_delete=models.SET_NULL)
    favorite_activities = models.ManyToManyField(Activity, blank=True)


    preferred_gender_match = models.ForeignKey(PrefGenderMatch,null=True, blank=True, on_delete=models.SET_NULL)
    age_range_min = models.IntegerField(default=18)
    age_range_max = models.IntegerField(default=99)
    open_to_romance = models.BooleanField(default=False)
    open_to_friendship = models.BooleanField(default=True)
    languages_spoken = models.ManyToManyField(Language, blank=True)
    travel_with = models.ForeignKey(TravelWith,null=True, blank=True, on_delete=models.SET_NULL)
    traveler_persona = models.ForeignKey(TravelPersona,null=True, blank=True, on_delete=models.SET_NULL)
    travel_energy_adventure = models.IntegerField(default=50)  # 0–100
    travel_energy_planning = models.IntegerField(default=50)
    travel_energy_social = models.IntegerField(default=50)

    travel_priorities = models.ManyToManyField(TravelPriority, blank=True)

    departure_location = models.CharField(max_length=255, blank=True)

    luggage_style = models.ForeignKey(LuggageStyle, on_delete=models.SET_NULL, null=True, blank=True)
    accommodation_preference = models.ManyToManyField(AccommodationPreference, blank=True)
    photo_sharing = models.ForeignKey(PhotoSharingPreference, on_delete=models.SET_NULL, null=True, blank=True)

    dream_destinations = models.ManyToManyField(DreamDestination, blank=True)

    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Profile of {self.user.username}"
