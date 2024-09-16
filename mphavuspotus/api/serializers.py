from rest_framework import serializers
from teams.models import Team

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['team_id', 'team_name', 'sport', 'coach_id', 'image']

from performance.models import Performance  

class PerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Performance
        fields = '__all__'
from video_records.models import VideoRecord


# Define a new serializer class inheriting from ModelSerializer
class VideoRecordSerializer(serializers.ModelSerializer):
   # Define a nested class Meta to configure the serializer's behavior
   class Meta:
       # Specify the model that this serializer will be working with
       model = VideoRecord
       # Include all fields from the VideoRecord model in the serialized output
       fields = '__all__'
from players.models import Players
from rest_framework import serializers
from django.contrib.auth.models import User as DjangoUser
from user.models import User

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Players
        fields = '__all__'      

class UserRegistrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password', 'role']

    def create(self, validated_data):
        # Create a DjangoUser object
        django_user = DjangoUser.objects.create_user(
            username=validated_data['email'],  # Using email as username
            email=validated_data['email'],
            password=validated_data['password'],
        )

        # Create the custom User object linked to the DjangoUser
        custom_user = User.objects.create(
            user=django_user,
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'], 
            # role=validated_data['role'],
        )

        return custom_user





class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

class ResetPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()


class MinimalUseSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['user_id', 'first_name', 'last_name', 'role']
        fields = '__all__'
