from django.db import models


class Performance(models.Model):
    performance_id = models.AutoField(primary_key=True)
    player_id = models.PositiveSmallIntegerField()
    passing_game = models.IntegerField()
    flying_ball = models.IntegerField()
    assists = models.IntegerField()
    goals = models.IntegerField()
    ball_control = models.PositiveIntegerField()
    group_defense = models.PositiveIntegerField()
    completion_of_action = models.IntegerField()
    team_attack = models.IntegerField(default=0)
    
    
def __str__(self):
        return f"Performance {self.performance_id} for Player {self.player_id}"
