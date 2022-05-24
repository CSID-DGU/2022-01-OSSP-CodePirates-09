from django.shortcuts import render
# from rest_framework.views import APIView
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from .models import UserInfo, UserPreference, UserPartner
from .serializers import UserInfoSerializer, UserPreferenceSerializer, UserPartnerSerializer
from rest_framework.parsers import JSONParser

import json


@csrf_exempt
def user_list(request):
    if request.method == 'GET':
        query_set = UserInfo.objects.all()
        serializer = UserInfoSerializer(query_set, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserInfoSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def user(request, userId):
    obj = UserInfo.objects.get(userId=userId)

    if request.method == 'GET':
        serializer = UserInfoSerializer(obj)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = UserInfoSerializer(obj, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        obj.delete()
        return HttpResponse(status=204)


@csrf_exempt
def signup(request):
    data = json.loads(request.body)

    return JsonResponse({'message': '회원 가입 성공'}, status=201)


@csrf_exempt
def signin(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        search_userId = data['userId']
        obj = UserInfo.objects.get(userId=search_userId)
        if data['userPassword'] == obj.userPassword:
            return HttpResponse(status=200)
        else:
            return HttpResponse(status=400)
