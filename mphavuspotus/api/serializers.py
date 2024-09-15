from rest_framework import serializers
from video_records.models import VideoRecord


# Define a new serializer class inheriting from ModelSerializer
class VideoRecordSerializer(serializers.ModelSerializer):
   # Define a nested class Meta to configure the serializer's behavior
   class Meta:
       # Specify the model that this serializer will be working with
       model = VideoRecord
       # Include all fields from the VideoRecord model in the serialized output
       fields = '__all__'
