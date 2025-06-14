from django.db import models
from django.core.exceptions import ValidationError
from apps.users.models import User

class UserMatch(models.Model):
    user1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='matches_initiated')
    user2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='matches_received')
    matched_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        unique_together = ('user1', 'user2')

    def clean(self):
        if self.user1 == self.user2:
            raise ValidationError("User cannot match with themselves.")
        if UserMatch.objects.filter(user1=self.user2, user2=self.user1).exists():
            raise ValidationError("Match already exists in opposite direction.")

    def __str__(self):
        return f"Match: {self.user1.username} & {self.user2.username}"


class MatchMessage(models.Model):
    match = models.ForeignKey(UserMatch, on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Message from {self.sender.username} at {self.sent_at.strftime('%Y-%m-%d %H:%M')}"
