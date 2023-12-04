from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _



class CustomUser(AbstractUser):
    image = models.ImageField(null=True)
    def __str__(self):
        return self.email
