from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from .views import Default

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', Default.as_view()),

    path('User/', include('User.urls')),
    path('Course/', include('Course.urls')),

    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
