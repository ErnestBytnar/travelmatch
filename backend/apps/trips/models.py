import uuid
from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.utils.translation import gettext_lazy as _
from apps.users.models import User

class TravelStyle(models.TextChoices):
    BACKPACKING = 'backpacking', _('Backpacking')
    LUXURY = 'luxury', _('Luxury')
    ROADTRIP = 'roadtrip', _('Road Trip')
    SLOW = 'slow_travel', _('Slow Travel')
    DIGITAL_NOMAD = 'nomad', _('Digital Nomad')

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Trip(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owned_trips')
    destination_city = models.CharField(max_length=100)
    destination_country = models.CharField(max_length=100)
    destination_place = models.CharField(max_length=255, blank=True)

    start_date = models.DateField()
    end_date = models.DateField()
    time = models.TimeField(null=True, blank=True)
    description = models.TextField(blank=True)

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    trip_tags = models.ManyToManyField(Tag, blank=True)

    max_participants = models.IntegerField(null=True, blank=True)

    preferred_travel_styles = ArrayField(models.CharField(max_length=50, choices=TravelStyle.choices), default=list, blank=True)
    preferred_activities = ArrayField(models.CharField(max_length=50), default=list, blank=True)
    preferred_gender = models.CharField(max_length=20, choices=[
        ('any', 'Any'), ('male', 'Male'), ('female', 'Female'), ('nonbinary', 'Non-binary')
    ], default='any')
    preferred_age_range_min = models.IntegerField(default=18)
    preferred_age_range_max = models.IntegerField(default=99)

    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    start_latitude = models.FloatField(null=True, blank=True)
    start_longitude = models.FloatField(null=True, blank=True)
    slug = models.SlugField(unique=True, blank=True)
    uuid = models.UUIDField(default=uuid.uuid4, unique=True)

    show_on_map = models.BooleanField(default=True)

    class Meta:
        indexes = [
            models.Index(fields=['destination_city']),
            models.Index(fields=['start_date', 'end_date']),
        ]
        ordering = ['-start_date']

    def __str__(self):
        return f"{self.destination_city}, {self.destination_country} ({self.start_date} - {self.end_date})"

    def save(self, *args, **kwargs):
        if not self.slug:
            # automatyczne generowanie slug, np. z miasta i daty
            from django.utils.text import slugify
            base_slug = slugify(f"{self.destination_city}-{self.start_date}")
            slug = base_slug
            num = 1
            while Trip.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{num}"
                num += 1
            self.slug = slug
        super().save(*args, **kwargs)


class TripParticipant(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name='participants')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='joined_trips')
    joined_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[
        ('pending', 'Pending'), ('accepted', 'Accepted'), ('rejected', 'Rejected')
    ], default='pending')

    class Meta:
        unique_together = ('trip', 'user')
        ordering = ['-joined_at']

    def __str__(self):
        return f"{self.user.username} - {self.trip.destination_city} ({self.status})"
