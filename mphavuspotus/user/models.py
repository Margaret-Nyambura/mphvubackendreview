from django.db import models
from django.contrib.auth.models import User as DjangoUser

# Define choices for roles
COACH = 'Coach'
AGENT = 'Agent'

ROLE_CHOICES = [
    (COACH, 'Coach'),
    (AGENT, 'Agent'),
]

class User(models.Model):
    user = models.OneToOneField(DjangoUser, on_delete=models.CASCADE, default=1)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    role = models.CharField(
        max_length=10,
        choices=ROLE_CHOICES,
        default=COACH,
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"