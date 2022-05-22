from django.shortcuts import render
from rest_framework.views import APIView
from .models import UserInfo


class SignUp(APIView):
    def get(self, request):
        return render(request, "User/signup.html")

    def post(self, request):
        # 구현
        return render(request, "User/signup.html")


class SignIn(APIView):
    def get(self, request):
        return render(request, "User/signin.html")

    def post(self, request):
        # 구현
        return render(request, "User/signin.html")
