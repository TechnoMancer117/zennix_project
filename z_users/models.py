from django.db import models

# Create seus models aqui.
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class CustomUser(AbstractUser):
    groups = models.ManyToManyField(
        Group,
        related_name='customuser_set',  # Adiciona um nome único para o relacionamento
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_permissions_set',  # Adiciona um nome único para o relacionamento
        blank=True
    )
