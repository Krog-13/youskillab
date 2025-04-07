from django.contrib.auth.models import User
from django.db import models


class HealthCard(models.Model):
    """Medical card model"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    weight = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        verbose_name="Weight (kg)",
        help_text="Patient's weight in kilograms (e.g., 70.50)"
    )
    height = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        verbose_name="Height (cm)",
        help_text="Patient's height in centimeters (e.g., 175.30)"
    )
    # Basic blood tests
    hemoglobin = models.DecimalField(
        max_digits=5,
        decimal_places=1,
        null=True,
        blank=True,
        verbose_name="Hemoglobin (g/L)",
        help_text="Hemoglobin level in blood (e.g., 130.5 g/L)"
    )
    leukocytes = models.DecimalField(
        max_digits=5,
        decimal_places=1,
        null=True,
        blank=True,
        verbose_name="Leukocytes (10⁹/L)",
        help_text="White blood cell count (e.g., 7.5 x 10⁹/L)"
    )
    erythrocytes = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name="Erythrocytes (10¹²/L)",
        help_text="Red blood cell count (e.g., 4.50 x 10¹²/L)"
    )
    glucose = models.DecimalField(
        max_digits=4,
        decimal_places=1,
        null=True,
        blank=True,
        verbose_name="Glucose (mmol/L)",
        help_text="Blood sugar level (e.g., 5.5 mmol/L)"
    )
    iron = models.DecimalField(
        max_digits=5,
        decimal_places=1,
        null=True,
        blank=True,
        verbose_name="Iron (µmol/L)",
        help_text="Serum iron level (e.g., 15.0 µmol/L)"
    )
    vitamin_d3 = models.DecimalField(
        max_digits=5,
        decimal_places=1,
        null=True,
        blank=True,
        verbose_name="Vitamin D3 (ng/mL)",
        help_text="25-hydroxyvitamin D level (e.g., 30.0 ng/mL)"
    )
    # Basic stool tests
    fecal_occult_blood = models.BooleanField(
        default=False,
        verbose_name="Fecal Occult Blood",
        help_text="Presence of hidden blood in stool (True/False)"
    )
    fecal_calprotectin = models.DecimalField(
        max_digits=5,
        decimal_places=1,
        null=True,
        blank=True,
        verbose_name="Calprotectin (µg/g)",
        help_text="Marker of inflammation in stool (e.g., 50.0 µg/g)"
    )
    # Data recording date
    date_recorded = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Date Recorded",
        help_text="When this data was recorded"
    )

# class OrganHeathCard(models.Model):
#     """Organization health card model"""
#     health_card = models.OneToOneField(HealthCard, on_delete=models.CASCADE)
