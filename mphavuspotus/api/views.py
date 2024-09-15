from rest_framework.views import APIView 
from rest_framework.response import Response 
from rest_framework import status 
from video_records.models import VideoRecord 
from .serializers import VideoRecordSerializer
# Define a class-based view for handling the list of video records.
class VideoRecordListView(APIView):
    # Handle GET requests to retrieve a list of video records.
    def get(self, request):
        # Retrieve all VideoRecord instances from the database.
        video_records = VideoRecord.objects.all()
        # Serialize the list of video records. 'many=True' indicates multiple records.
        serializer = VideoRecordSerializer(video_records, many=True)
        # Return the serialized data as a JSON response.
        return Response(serializer.data)
    # Handle POST requests to create a new video record.
    def post(self, request):
        # Initialize the serializer with the incoming data from the request.
        serializer = VideoRecordSerializer(data=request.data)
        # Check if the provided data is valid according to the serializer's rules.
        if serializer.is_valid():
            # Save the new video record to the database.
            serializer.save()
            # Return a successful response with the created record's data and HTTP 201 status.
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # Return a response with validation errors and HTTP 400 status if the data is invalid.
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class VideoRecordDetailView(APIView):
    # Handle GET requests to retrieve a specific video record by ID.
    def get(self, request, video_record_id):
        # Check if the video record with the given ID exists.
        if VideoRecord.objects.filter(pk=video_record_id).exists():
            # Retrieve the VideoRecord instance.
            video_record = VideoRecord.objects.get(pk=video_record_id)
            # Serialize the video record.
            serializer = VideoRecordSerializer(video_record)
            # Return the serialized data as a JSON response.
            return Response(serializer.data)
        else:
            # Return HTTP 404 status if the record is not found.
            return Response(status=status.HTTP_404_NOT_FOUND)

    # Handle PUT requests to update a specific video record by ID.
    def put(self, request, video_record_id):
        # Check if the video record with the given ID exists.
        if VideoRecord.objects.filter(pk=video_record_id).exists():
            # Retrieve the VideoRecord instance.
            video_record = VideoRecord.objects.get(pk=video_record_id)
            # Initialize the serializer with the updated data.
            serializer = VideoRecordSerializer(video_record, data=request.data)
            # Check if the updated data is valid.
            if serializer.is_valid():
                # Save the updated video record to the database.
                serializer.save()
                # Return a successful response with the updated record's data and HTTP 200 status.
                return Response(serializer.data, status=status.HTTP_200_OK)
            # Return HTTP 400 status if the data is invalid.
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            # Return HTTP 404 status if the record is not found.
            return Response(status=status.HTTP_404_NOT_FOUND)

    # Handle DELETE requests to delete a specific video record by ID.
    def delete(self, request, video_record_id):
        # Check if the video record with the given ID exists.
        if VideoRecord.objects.filter(pk=video_record_id).exists():
            # Retrieve the VideoRecord instance.
            video_record = VideoRecord.objects.get(pk=video_record_id)
            # Delete the video record from the database.
            video_record.delete()
            # Return HTTP 204 status indicating successful deletion and no content.
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            # Return HTTP 404 status if the record is not found.
            return Response(status=status.HTTP_404_NOT_FOUND)


