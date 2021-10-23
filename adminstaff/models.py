from django.db import models
from django.utils import timezone

# Create your models here


def filepath(request, filename):
    old_filename = filename


class AddItem(models.Model):
    name = models.CharField(max_length=200, default='none')
    price = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    comp = models.CharField(max_length=200, default='none')
    category = models.DateTimeField(default=timezone.now)
    image = models.CharField(max_length=200, default='none')
    objects = None

    def __str__(self):
        return self.name


class Orders(models.Model):
    food = models.CharField(max_length=200, default='none')
    quantity = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    name = models.CharField(max_length=200, default='none')
    phone_number = models.DateTimeField(default=timezone.now)
    Address = models.CharField(max_length=200, default='none')
    price = models.CharField(max_length=200, default='none')
    status = models.CharField(max_length=200, default='pending')
    objects = None

    def __str__(self):
        return self.name


class StaffUser(models.Model):
    email = models.EmailField(max_length=200, default='none')
    password = models.CharField(max_length=200, default='none')

    objects = None
    def __str__(self):
        return self.email