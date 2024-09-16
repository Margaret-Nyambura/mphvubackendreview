
from django.db import models

class Players(models.Model):
    name = models.CharField(max_length=100)
    date_of_birth = models.DateTimeField()
    # team = models.ForeignKey(Team, on_delete=models.CASCADE) 
    position = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.name}"
    