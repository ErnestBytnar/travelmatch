# Generated by Django 5.1.3 on 2025-05-29 15:27

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination_city', models.CharField(max_length=100)),
                ('destination_country', models.CharField(max_length=100)),
                ('destination_place', models.CharField(blank=True, max_length=255)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('time', models.TimeField(blank=True, null=True)),
                ('description', models.TextField(blank=True)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('trip_tags', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=50), blank=True, default=list, size=None)),
                ('max_participants', models.IntegerField(blank=True, null=True)),
                ('preferred_travel_styles', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(choices=[('backpacking', 'Backpacking'), ('luxury', 'Luxury'), ('roadtrip', 'Road Trip'), ('slow_travel', 'Slow Travel'), ('nomad', 'Digital Nomad')], max_length=50), blank=True, default=list, size=None)),
                ('preferred_activities', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=50), blank=True, default=list, size=None)),
                ('preferred_gender', models.CharField(choices=[('any', 'Any'), ('male', 'Male'), ('female', 'Female'), ('nonbinary', 'Non-binary')], default='any', max_length=20)),
                ('preferred_age_range_min', models.IntegerField(default=18)),
                ('preferred_age_range_max', models.IntegerField(default=99)),
            ],
        ),
        migrations.CreateModel(
            name='TripParticipant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('joined_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('accepted', 'Accepted'), ('rejected', 'Rejected')], default='pending', max_length=20)),
            ],
        ),
    ]
