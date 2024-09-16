from django.db import models  
# Import the models module from Django. This module provides classes and functions to define and manage database models.
class VideoRecord(models.Model):
    # Defines an integer field that serves as the primary key for the model.
   video_record_id = models.AutoField(primary_key=True)
    # Defines a foreign key field that links to the Player model. The 'on_delete=models.CASCADE' argument specifies that if a referenced Player is deleted, all related VideoRecord instances should also be deleted.
   player_id = models.PositiveSmallIntegerField() #supposed to be a foreign key
# Defines a text field named 'video_description' to store the description of the video record.
   video_description = models.TextField() 
# Defines a file field named 'video_file' to store the uploaded video file. The 'upload_to' argument specifies the directory within which the file will be stored. 'null=True' allows this field to be empty in the database, and 'blank=True' allows it to be empty in forms.
   video_file = models.FileField(upload_to='videos/', null=True, blank=True)# video_file = models.FileField(upload_to='videos/', default='path/to/default/file.mp4')
# Defines a float field named 'shooting_accuracy' with a default value of 0.0 to represent the accuracy of the shooting in the video record.
   shooting_accuracy = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
   # Defines a float field named 'shooting_angle' with a default value of 0.0 to represent the angle of shooting in the video record.
   shooting_angle = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
   # Defines the string representation of the VideoRecord model.
def __str__(self):
        # Returns a string that includes the video record ID and the associated player ID when the object is represented as a string.
    return f"VideoRecord {self.video_record_id} by {self.player_id}"
