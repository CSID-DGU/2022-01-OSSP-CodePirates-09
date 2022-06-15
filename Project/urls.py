from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from .views import Default
from Project import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', Default.as_view()),

    path('User/', include('User.urls')),
    path('main', views.main),
    path('default', views.default),
    path('signup', views.signup),
    path('signin', views.signin)

]
