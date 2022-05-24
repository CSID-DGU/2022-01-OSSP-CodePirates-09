from django.shortcuts import render
# from rest_framework.views import APIView
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import UserInfo, UserPreference, UserPartner
from .serializers import UserInfoSerializer, UserPreferenceSerializer, UserPartnerSerializer
from rest_framework.parsers import JSONParser


@csrf_exempt
class SignUp():
    def post(self, request):
        pass


class SignIn():
    def get(self, request):
        pass

<<<<<<< HEAD
# class SignUp(APIView):
#     def get(self, request):
#         return render(request, "User/signup.html")
#
#     def post(self, request):
#         # 구현
#         return render(request, "User/signup.html")
#
#
# class SignIn(APIView):
#     def get(self, request):
#         return render(request, "User/signin.html")
#
#     def post(self, request):
#         # 구현
#         return render(request, "User/signin.html")
=======
    def post(self, request):
        # 구현
        return render(request, "User/signin.html")
>>>>>>> 304fb26aeb2e0ab653765633567c12ccaf8b80a2
