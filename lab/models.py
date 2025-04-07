from django.contrib.auth.models import User
from django.db import models as dj_models
from .health import models
from .skill import models


class Profile(dj_models.Model):
    """Profile model"""
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female')
    )
    user = dj_models.OneToOneField(User, on_delete=dj_models.CASCADE)
    birthday = dj_models.DateField("birthday")
    phone_number = dj_models.CharField("phone number", max_length=20, blank=True, null=True)
    gender = dj_models.CharField("gender", max_length=1, choices=GENDER_CHOICES)
    avatar = dj_models.ImageField("avatar", upload_to="avatar", null=True, blank=True)
