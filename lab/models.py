from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    """Profile model"""
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birthday = models.DateField("birthday")
    phone_number = models.CharField("phone number", max_length=20, blank=True, null=True)
    gender = models.CharField("gender", max_length=1, choices=GENDER_CHOICES)
    avatar = models.ImageField("avatar", upload_to="avatar", null=True, blank=True)
