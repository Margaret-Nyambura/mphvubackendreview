
from django.urls import path
from .views import TeamListView, TeamDetailView

urlpatterns = [
    path('teams/', TeamListView.as_view(), name='team-list'), 
    path('teams/<int:team_id>/', TeamDetailView.as_view(), name='team-detail'),
]
from django.urls import path, include
from .views import PerformanceListView, PerformanceView 
urlpatterns = [
    path('performance/', PerformanceListView.as_view(), name='performance-list'),

    # URL pattern for retrieving, updating, or deleting a specific performance by player_id and performance_id
    path('performance/<int:player_id>/<int:performance_id>/', PerformanceView.as_view(), name='performance-detail'),

    # Optional: URL pattern for retrieving all performances of a specific player
    path('performance/<int:player_id>/', PerformanceView.as_view(), name='player-performance-list'),
]
from django.urls import path 
from .views import VideoRecordListView, VideoRecordDetailView


# Define a list of URL patterns to map URLs to views.
urlpatterns = [
#  This view handles the list of video records. The name 'video_record_list' is used for reverse URL resolution.
   path('video_records/', VideoRecordListView.as_view(), name='video_record_list'),
   # This view handles individual video record details. The '<int:video_record_id>' part captures an integer from the URL and passes it to the view. The name 'video_record_detail' is used for reverse URL resolution.
   path('video_records/<int:video_record_id>/', VideoRecordDetailView.as_view(), name='video_record_detail'),
]

from django.urls import path
from .views import PlayerListView, PlayerDetailView
from django.contrib import admin
from api.views import RegisterUser, LoginUser, ResetPasswordView, UserListView, UserDetailView

urlpatterns = [
    path('players/', PlayerListView.as_view(), name='player_list'),  # URL pattern for listing and creating players
    path('players/<int:player_id>/', PlayerDetailView.as_view(), name='player_detail'),  # URL pattern for retrieving, updating, and deleting a player
    # path('admin/', admin.site.urls),
    path('user/', UserListView.as_view(), name='user_list'),  
    path('user/<int:id>/', UserDetailView.as_view(), name='user_detail'),
    path('user/register/', RegisterUser.as_view(), name='register'),
    path('user/login/', LoginUser.as_view(), name='login'), 
    path('user/reset_password/', ResetPasswordView.as_view(), name='reset_password'), 
    path('api/user/', UserListView.as_view(), name='user-list'),
    
]
