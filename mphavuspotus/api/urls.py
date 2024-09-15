from django.urls import path 
from .views import VideoRecordListView, VideoRecordDetailView


# Define a list of URL patterns to map URLs to views.
urlpatterns = [
#  This view handles the list of video records. The name 'video_record_list' is used for reverse URL resolution.
   path('video_records/', VideoRecordListView.as_view(), name='video_record_list'),
   # This view handles individual video record details. The '<int:video_record_id>' part captures an integer from the URL and passes it to the view. The name 'video_record_detail' is used for reverse URL resolution.
   path('video_records/<int:video_record_id>/', VideoRecordDetailView.as_view(), name='video_record_detail'),
]
