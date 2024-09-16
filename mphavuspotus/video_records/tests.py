from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from video_records.models import VideoRecord

class VideoRecordTests(APITestCase):
    def setUp(self):
        # Create an in-memory file object for testing
        self.test_file = SimpleUploadedFile("test_video.mp4", b"file_content", content_type="video/mp4")

        self.video_record = VideoRecord.objects.create(
            player_id=1,
            video_description="Test video",
            video_file=self.test_file,
            shooting_accuracy=0.75,
            shooting_angle=0.45
        )
        self.list_url = reverse('video_record_list')
        self.detail_url = reverse('video_record_detail', kwargs={'video_record_id': self.video_record.video_record_id})

    def test_list_video_records(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['video_description'], "Test video")

    def test_create_video_record(self):
        # Create a new in-memory file for the test
        new_file = SimpleUploadedFile("new_video.mp4", b"new_file_content", content_type="video/mp4")
        
        data = {
            'player_id': 2,
            'video_description': 'New test video',
            'video_file': new_file,  # Use SimpleUploadedFile here
            'shooting_accuracy': 0.85,
            'shooting_angle': 0.55
        }
        response = self.client.post(self.list_url, data, format='multipart')  # Use 'multipart' format for file uploads
        print(response.data)  # Add this line to debug
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(VideoRecord.objects.count(), 2)
        self.assertEqual(VideoRecord.objects.latest('video_record_id').video_description, 'New test video')

    def test_get_video_record(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['video_description'], "Test video")

    def test_update_video_record(self):
        updated_file = SimpleUploadedFile("updated_video.mp4", b"updated_content", content_type="video/mp4")
        data = {
            'player_id': 1,
            'video_description': 'Updated test video',
            'video_file': updated_file,  # Use SimpleUploadedFile here
            'shooting_accuracy': 0.90,
            'shooting_angle': 0.60
        }
        response = self.client.put(self.detail_url, data, format='multipart')  # Use 'multipart' format for file uploads
        print(response.data)  # Add this line to debug
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.video_record.refresh_from_db()
        self.assertEqual(self.video_record.video_description, 'Updated test video')

    def test_delete_video_record(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(VideoRecord.objects.count(), 0)

    def test_get_nonexistent_video_record(self):
        non_existent_url = reverse('video_record_detail', kwargs={'video_record_id': 999})
        response = self.client.get(non_existent_url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)