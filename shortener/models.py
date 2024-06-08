from django.db import models

# Create your models here.

class URL(models.Model):
    long_url = models.URLField(null=False, blank=False)

    # Max Length is 8 for custom urls
    # Will use only 7 char for generated short url
    short_url = models.CharField(max_length=8, null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True)

    # For 8 characters long custom url, we need a validated user
    # Will implement later
    user_id = models.CharField(null=True, max_length=10)
