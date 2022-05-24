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