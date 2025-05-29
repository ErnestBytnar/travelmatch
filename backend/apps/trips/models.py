from django.db import models


from django.utils.translation import gettext_lazy as _
from django.contrib.postgres.fields import ArrayField


# Create your models here.


class TravelStyle(models.TextChoices):
    BACKPACKING = 'backpacking', _('Backpacking')
    LUXURY = 'luxury', _('Luxury')
    ROADTRIP = 'roadtrip', _('Road Trip')
    SLOW = 'slow_travel', _('Slow Travel')
    DIGITAL_NOMAD = 'nomad', _('Digital Nomad')


class Trip(models.Model):
    owner = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='owned_trips')
    destination_city = models.CharField(max_length=100)
    destination_country = models.CharField(max_length=100)
    destination_place = models.CharField(max_length=255, blank=True)

    start_date = models.DateField()
    end_date = models.DateField()
    time = models.TimeField(null=True, blank=True)
    description = models.TextField(blank=True)

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    trip_tags = ArrayField(models.CharField(max_length=50), default=list, blank=True)
    max_participants = models.IntegerField(null=True, blank=True)

    # preferencje co do uczestników (do lepszego matchowania)
    preferred_travel_styles = ArrayField(models.CharField(max_length=50, choices=TravelStyle.choices), default=list, blank=True)
    preferred_activities = ArrayField(models.CharField(max_length=50), default=list, blank=True)
    preferred_gender = models.CharField(max_length=20, choices=[
        ('any', 'Any'), ('male', 'Male'), ('female', 'Female'), ('nonbinary', 'Non-binary')
    ], default='any')
    preferred_age_range_min = models.IntegerField(default=18)
    preferred_age_range_max = models.IntegerField(default=99)

    class Meta:
        indexes = [
            models.Index(fields=['destination_city']),
            models.Index(fields=['start_date', 'end_date']),
        ]


class TripParticipant(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name='participants')
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='joined_trips')
    joined_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[
        ('pending', 'Pending'), ('accepted', 'Accepted'), ('rejected', 'Rejected')
    ], default='pending')

    class Meta:
        unique_together = ('trip', 'user')