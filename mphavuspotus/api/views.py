from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from players.models import Players
from rest_framework.views import APIView
from .serializers import PlayerSerializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
import json
from django.contrib.auth import authenticate, login as auth_login
from django.core.mail import send_mail
from django.conf import settings
from .serializers import UserRegistrationSerializer, LoginSerializer, ResetPasswordSerializer, MinimalUseSerializer
from user.models import User

# Handles listing and creating players
class PlayerListView(APIView):

    def get(self, request):
        # Retrieves and returns a list of all players
        players = Players.objects.all()
        serializer = PlayerSerializer(players, many=True)
        return Response(serializer.data)

    def post(self, request):
        # Creates a new player with the provided data
        serializer = PlayerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Handles retrieval, update, and deletion of a single player

class PlayerDetailView(APIView):
    
    def get(self, request, player_id):
        # Retrieves and returns a single player by ID
        player = self.get_object(player_id)
        serializer = PlayerSerializer(player)
        return Response(serializer.data)
    
    def put(self, request, player_id):
        # Updates an existing player with the provided data
        player = self.get_object(player_id)
        serializer = PlayerSerializer(player, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, player_id):
        # Deletes a player by ID
        player = self.get_object(player_id)
        player.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def get_object(self, player_id):
        # Retrieves a player by ID or raises 404 if not found
        from django.shortcuts import get_object_or_404
        return get_object_or_404(Players, pk=player_id)


    


class RegisterUser(APIView):
    def post(self, request):
        serializer = UserRegistrationSerializer(data = data)
        if serializer.is_valid():
            if User.objects.filter(username=username).exists():
                return Response({'error': 'Username already exists'}, status=status.HTTP_400_BAD_REQUEST)

            serializer.save()
            return Response({'status': 'User created'}, status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)    
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):

        # Handle fetching users (GET)
        users = User.objects.all()  # Get all users
        serializer = UserRegistrationSerializer(users, many=True)  # Serialize all users
        return Response(serializer.data, status=status.HTTP_200_OK)    

class LoginUser(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']
            user = authenticate(username=username, password=password)
            if user:
                auth_login(request, user)
                return Response({'detail': 'Login successful'}, status=status.HTTP_200_OK)
            return Response({'detail': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ResetPasswordView(APIView):
    def post(self, request):
        serializer = ResetPasswordSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            user = User.objects.filter(email=email).first()
            if user:
                send_mail(
                    'Password Reset Request',
                    'Follow the link to reset your password.',
                    settings.DEFAULT_FROM_EMAIL,
                    [email],
                )
                return Response({'detail': 'Password reset email sent'}, status=status.HTTP_200_OK)
            return Response({'detail': 'Email not found'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserRoleView(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = MinimalUseSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class UserListView(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = MinimalUseSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserListView(APIView):
    def get(self, request):
        users = User.objects.all()
        email = request.query_params.get("email")
        if email:
            users = users.filter(email=email)
        serializer = UserRegistrationSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetailView(APIView):
    def get(self, request, id):
        user = get_object_or_404(User, id=id)
        serializer = UserRegistrationSerializer(user)
        return Response(serializer.data)

    def put(self, request, id):
        user = get_object_or_404(User, id=id)
        serializer = UserRegistrationSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        user = get_object_or_404(User, id=id)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def post(self, request, id):
        user = get_object_or_404(User, id=id)
        action = request.data.get("action")
        if action == "some_custom_action":
            # Implement custom logic here
            return Response({'status': 'Custom action executed'}, status=status.HTTP_200_OK)
        return Response({'error': 'Invalid action'}, status=status.HTTP_400_BAD_REQUEST)   
    
    
    
    
