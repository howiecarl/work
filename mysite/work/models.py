# Core django imports
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User


class Photo(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=255, blank=True)
    website = models.URLField(max_length=200)
    description = models.TextField()
    image = models.ImageField(blank=True, null=True, upload_to="media/uploads/%s")
