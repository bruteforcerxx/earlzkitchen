from django.db import models
from django.utils import timezone

# Create your models here


class ContactMessages(models.Model):
    first_name = models.CharField(max_length=200, default='john')
    email = models.EmailField(max_length=250, blank=True, null=True)
    message = models.CharField(max_length=200, default='doe')
    date_created = models.DateTimeField(default=timezone.now)
    objects = None

    def __str__(self):
        return self.email


class NewsLetter(models.Model):
    email = models.EmailField(max_length=250, blank=True, null=True)
    date_created = models.DateTimeField(default=timezone.now)
    objects = None

    def __str__(self):
        return self.email