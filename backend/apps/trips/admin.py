from django.contrib import admin

from apps.trips.models import TripParticipant,Trip

# Register your models here.

admin.site.register(Trip)
admin.site.register(TripParticipant)