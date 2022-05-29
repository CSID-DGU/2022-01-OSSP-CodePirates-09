from django.urls import path
from User import views

urlpatterns = [
    path('user_list/', views.user_list),
    path('user/<str:userId>/', views.user),
    path('signin/', views.signin),
    path('signup/', views.signup),
    path('findid/', views.findid)
]
