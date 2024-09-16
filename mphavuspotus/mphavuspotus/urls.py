"""
URL configuration for mphavuspotus project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  # Map the URL path 'admin/' to Django's built-in admin interface.
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    
    # Map the URL path 'api/' to the URL configuration defined in the 'api.urls' module.
    path('api/', include('api.urls')),
    ]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from api.views import RegisterUser, LoginUser, ResetPasswordView, UserListView, UserDetailView

urlpatterns = [
 
    path('api/', include('api.urls')),
    path('admin/', admin.site.urls),
    path('api/user/', UserListView.as_view(), name='user_list'),  # Handles /api/user/ for listing users
    path('api/user/<int:id>/', UserDetailView.as_view(), name='user_detail'),  # Handles /api/user/<id>/ for user details
    path('api/user/register/', RegisterUser.as_view(), name='register'),  # Handles /api/user/register/ for registration
    path('api/user/login/', LoginUser.as_view(), name='login'),  # Handles /api/user/login/ for login
    path('api/user/reset_password/', ResetPasswordView.as_view(), name='reset_password'),  # Handles /api/user/reset_password/ for password reset
    path('accounts/', include('allauth.urls')),  
    path('auth/', include('authentication.urls')),  
]
