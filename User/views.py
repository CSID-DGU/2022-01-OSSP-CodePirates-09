from django.shortcuts import render
# from rest_framework.views import APIView
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
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
        serializer =UserInfoSerializer(obj)
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
    if request.method == 'POST':
        data = JSONParser().parse(request) # 넘어온 requset들을 Json 형태로 변환

        userinfo = { # userInfo과 preference로 나눈이유 - preference가 foreignkey로 참조하기 때문에 나눠서 저장
            "userName":  data.get("userName"),
            "userEmail": data.get("userEmail"),
            "userId": data.get("userId"),
            "userPassword": data.get("userPassword"),
            "userSex": data.get("userSex"),
            "userAge": data.get("userAge")
        }

        userinfo_serializer = UserInfoSerializer(data=userinfo) # userinfo로 저장한 딕셔너리형태 db에 저장
        if userinfo_serializer.is_valid():
            userinfo_serializer.save()
            preference = { # foreignkey로 참조한 자식테이블이기 때문에 나눠서 데이터 저장,
                # 그리고 userInfo가 선행되어서 저장되어야하기 때문에 if문으로 조건 진행
                "userId": data.get("userId"),
                "preferenceEat": data.get("preferenceEat"),
                "preferencePlay": data.get("preferencePlay"),
                "preferenceDrink": data.get("preferenceDrink"),
                "preferenceSee": data.get("preferenceSee"),
                "preferenceWalk": data.get("preferenceWalk")
            }
            prefer_serializer = UserPreferenceSerializer(data=preference) # preference로 저장한 딕셔너리형태 db에 저장
            if prefer_serializer.is_valid():
                prefer_serializer.save()
                return JsonResponse({'message': '회원 가입 성공'}, status=201) # 두 테이블이 모두 저장되면 회원가입 성공 !

        return HttpResponse({"message : Error"}, status=400) # 그렇지 않으면 실패


@csrf_exempt
def signin(request):
    if request.method == 'POST': # 메소드가 post로 넘어온 경우
        data = JSONParser().parse(request) # 로그인 화면에서 얻어온 값을 json형태로 저장

        if data.get('id') == "" or data.get('password') == "": # 아이디 비밀번호 중 입력값이 없는 경우
            return JsonResponse({'message' : '아이디 또는 비밀번호를 입력하세요.'}, status=400)

        if UserInfo.objects.filter(userId=data.get('id')).exists(): # 아이디가 같은 것이 있는지 확인
            login_user = UserInfo.objects.get(userId=data.get('id')) # 아이디가 같은것이 있으면, 객체로 저장

            if login_user.userPassword == data.get('password'): # 나중에는 bcrypt를 이용해서 암호화 할 예정
                return JsonResponse({'message' : '로그인 성공'}, status=201) # 성공시 render를 통해 메인화면으로 이동

            return JsonResponse({'message' : '비밀번호를 확인해주세요.'}, status=400) # 오류문 출력 이후, 로그인페이지로 이동
        return JsonResponse({'message' : '존재하지 않는 아이디 입니다.'}, status=400) # 다시 로그인 페이지로 이동

    return JsonResponse({'message' : 'Error'}, status=400) # 나중에는 render로 페이지 이동을 시킬 예정
