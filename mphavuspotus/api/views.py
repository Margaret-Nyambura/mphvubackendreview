from django.shortcuts import render

from performance.models import Performance
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import PerformanceSerializer

class PerformanceListView(APIView):
    def get(self, request):
        performances = Performance.objects.all()
        serializer = PerformanceSerializer(performances, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PerformanceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PerformanceView(APIView):
    def get(self, request, player_id, performance_id=None):
        if performance_id:
            performance = get_object_or_404(Performance, player_id=player_id, performance_id=performance_id)
            serializer = PerformanceSerializer(performance)
            return Response(serializer.data)
        else:
            performances = Performance.objects.filter(player_id=player_id)
            serializer = PerformanceSerializer(performances, many=True)
            return Response(serializer.data)

    def post(self, request, player_id):
        data = request.data.copy()
        data['player_id'] = player_id
        serializer = PerformanceSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, player_id, performance_id):
        performance = get_object_or_404(Performance, player_id=player_id, performance_id=performance_id)
        serializer = PerformanceSerializer(performance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, player_id, performance_id):
        performance = get_object_or_404(Performance, player_id=player_id, performance_id=performance_id)
        performance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
