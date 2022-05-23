from django.urls import path
from .views import SignIn, SignUp

urlpatterns = [
    path('signin', SignIn.as_view(), name='signin'),
    path('signup', SignUp.as_view(), name='signup')
]
