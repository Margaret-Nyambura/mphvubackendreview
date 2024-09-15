from django.urls import path, include
from .views import PerformanceListView, PerformanceView 
urlpatterns = [
    path('performance/', PerformanceListView.as_view(), name='performance-list'),

    # URL pattern for retrieving, updating, or deleting a specific performance by player_id and performance_id
    path('performance/<int:player_id>/<int:performance_id>/', PerformanceView.as_view(), name='performance-detail'),

    # Optional: URL pattern for retrieving all performances of a specific player
    path('performance/<int:player_id>/', PerformanceView.as_view(), name='player-performance-list'),
]
