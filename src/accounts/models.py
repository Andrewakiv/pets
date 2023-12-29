from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    photo = models.ImageField(upload_to='accounts/%Y/%m/%d/', blank=True, null=True)
    data_birth = models.DateTimeField(blank=True, null=True)
