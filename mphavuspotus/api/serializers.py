from rest_framework import serializers
from teams.models import Team

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['team_id', 'team_name', 'sport', 'coach_id', 'image']
