from django.db import models
from django.core.validators import RegexValidator

class AlowedUsers(models.Model):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone = models.CharField(validators=[phone_regex], max_length=13, unique=True) # Validators should be a list

    class Meta:
        ordering = ('phone',)

    def __str__(self):
        return self.phone