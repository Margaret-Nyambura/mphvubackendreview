
from django.urls import path
from .views import TeamListView, TeamDetailView

urlpatterns = [
    path('teams/', TeamListView.as_view(), name='team-list'), 
    path('teams/<int:team_id>/', TeamDetailView.as_view(), name='team-detail'),
]
