from django.db import models
from django.contrib.auth.models import User
from content.models import Content


class Like(models.Model):
    """
    Like model, related to 'owner' and 'text'.
    'owner' is a User instance and 'post' is a text instance.
    'unique_together' makes sure a user can't like the same text twice.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.ForeignKey(
        Content, related_name='likes', on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'text']

    def __str__(self):
        return f'{self.owner} {self.text}'