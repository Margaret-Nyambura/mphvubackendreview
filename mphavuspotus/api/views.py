
from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from teams.models import Team
from .serializers import TeamSerializer

# Define a view to handle operations on a list of teams
class TeamListView(APIView):
    # Handle GET requests to retrieve a list of all teams
    def get(self, request):
        # Retrieve all team instances from the database
        teams = Team.objects.all()
        # Serialize the list of teams into JSON format
        serializer = TeamSerializer(teams, many=True)
        # Return the serialized data in the response
        return Response(serializer.data)

    # Handle POST requests to create a new team
    def post(self, request):
        # Create a serializer instance with the data from the request
        serializer = TeamSerializer(data=request.data)
        # Check if the data is valid
        if serializer.is_valid():
            # Save the new team instance to the database
            serializer.save()
            # Return the serialized data of the newly created team and a 201 Created status code
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # If the data is invalid, return the errors and a 400 Bad Request status code
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Define a view to handle operations on a specific team identified by team_id
class TeamDetailView(APIView):
    # Handle GET requests to retrieve a specific team
    def get(self, request, team_id):
        # Attempt to retrieve the team instance with the given team_id
        team = Team.objects.filter(team_id=team_id).first()
        # Check if the team was found
        if team is not None:
            # Serialize the team instance into JSON format
            serializer = TeamSerializer(team)
            # Return the serialized data of the team
            return Response(serializer.data)
        # If the team was not found, return a 404 Not Found status code
        return Response(status=status.HTTP_404_NOT_FOUND)

    # Handle PUT requests to update a specific team
    def put(self, request, team_id):
        # Attempt to retrieve the team instance with the given team_id
        team = Team.objects.filter(team_id=team_id).first()
        # Check if the team was found
        if team is not None:
            # Create a serializer instance with the team and the updated data from the request
            serializer = TeamSerializer(team, data=request.data)
            # Check if the updated data is valid
            if serializer.is_valid():
                # Save the updated team instance to the database
                serializer.save()
                # Return the serialized data of the updated team
                return Response(serializer.data)
            # If the updated data is invalid, return the errors and a 400 Bad Request status code
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # If the team was not found, return a 404 Not Found status code
        return Response(status=status.HTTP_404_NOT_FOUND)

   