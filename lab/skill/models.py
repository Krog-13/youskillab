from django.contrib.auth.models import User
from django.db import models


class Portfolio(models.Model):
    """Portfolio model"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    job_title = models.CharField("job title", max_length=100, help_text="Your position, e.g., Software Engineer")
    company_name = models.CharField("company name", max_length=100, help_text="Name of the company")
