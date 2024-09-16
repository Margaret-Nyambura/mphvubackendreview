# Register your models here.
# This module provides the administrative interface for managing site content.
from django.contrib import admin 
 # Import the VideoRecord model from the current package's models module.
from .models import VideoRecord 
 # Register the VideoRecord model with Django's admin site.
admin.site.register(VideoRecord)
