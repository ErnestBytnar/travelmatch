# Generated by Django 5.1.3 on 2025-06-14 12:22

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('matching', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='matchmessage',
            name='sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='usermatch',
            name='user1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='matches_initiated', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='usermatch',
            name='user2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='matches_received', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='matchmessage',
            name='match',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='matching.usermatch'),
        ),
        migrations.AlterUniqueTogether(
            name='usermatch',
            unique_together={('user1', 'user2')},
        ),
    ]
