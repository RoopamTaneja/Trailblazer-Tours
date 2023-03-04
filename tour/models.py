from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import date


class Profile(models.Model):
    # CASCADE, if user gone then profile gone but not vice-versa
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dp = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f"{self.user.username} DP"


class Tour(models.Model):  # Tour is name of model or table
    users = models.ManyToManyField(User, related_name="tours")
    created_by = models.CharField(max_length=100, default="")
    tour_name = models.CharField(max_length=50, default="")
    desc = models.CharField(max_length=500, default="")

    def __str__(self):
        return self.tour_name


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=12)
    desc = models.TextField(max_length=500)
    date = models.DateField()
