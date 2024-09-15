from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class Coach(models.Model):
    name = models.CharField(max_length=100)

class Team(models.Model):
    team_id = models.AutoField(primary_key=True)
    team_name = models.CharField(max_length=100)
    sport = models.CharField(max_length=50)
    coach_id = models.ForeignKey(Coach, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to='team_images/', null=True, blank=True)

    def __str__(self):
        return self.team_name

