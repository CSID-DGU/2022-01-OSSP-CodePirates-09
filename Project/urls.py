from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from .views import Main, Default

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', Main.as_view()),
    path('default', Default.as_view()),

    path('User/', include('User.urls')),
    path('Course/', include('Course.urls')),

    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
