from django.db import models

from apps.users.models import User


# Create your models here.


class UserMatch(models.Model):
    user1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='matches_initiated')
    user2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='matches_received')
    match_score = models.IntegerField()
    status = models.CharField(max_length=20, choices=[
        ('pending', 'Pending'), ('matched', 'Matched'), ('rejected', 'Rejected')
    ])
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user1', 'user2')