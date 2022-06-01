from django.shortcuts import render
# from rest_framework.views import APIView
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
from django.views import View
from .models import UserInfo, UserPreference, UserPartner
from .serializers import UserInfoSerializer, UserPreferenceSerializer, UserPartnerSerializer
from rest_framework.parsers import JSONParser
from django.shortcuts import render, redirect



import re # 정규 표현식을 지원
import json
import bcrypt # 비밀번호 암호화를 위해서 패키지 다운로드

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

        for key, val in data.items(): # json은 key-value 형태 이기 때문에 key,val값으로 for문 진행
            if val == "" and key: # 만약 빈값으로 넘어온 밸류가 있다면 오류문 출력하고, 나중에 페이지 이동까지 구현
                return JsonResponse({'message': '입력되지 않은 항목이 있습니다.'}, status=400) # 나중에 페이지 이동 구현

        # if data.get('userId') != data.get('userIdCheck'): # 프론트에서 중복체크 버트를 누르면 checkid 실행, 거기서 checkid가 확정
        #     return JsonResponse({'message': '아이디 중복체크를 하지 않았습니다.'}, status=400)
        #
        # elif data.get('userPassword') != data.get('userPasswordCheck'): # 프론트에서 구현 가능한건인가 ?, 일단 비밀번호 비교
        #     return JsonResponse({'message' : '입력된 두 비밀번호가 다릅니다.'}, status=400)
        # else:
        #     regex = re.compile(r'^[a-zA-Z0-9+_.]+@[a-zA-Z0-9-]\.[a-zA-Z0-9-.]+$') # 정규표현을 적어서 이메일 유효성 검사
        #     vaildEmail = regex.search(data.get('userEmail')) # 입력받은 데이터를 정규표현에 대입하여 검사
        #     if vaildEmail == None: # 이메일 형식이 유효하지 않는 경우
        #         return JsonResponse({'message' : '이메일 형식이 올바르지 않습니다.'}, status=400) # 나중에 페이지 이동으로 구현


        # 여기 까지 진행 되었다는 것은 빈값이 넘어온 것이 없고, 아이디 중복체크도 진행했고, 비밀번호도 알맞게 입력한 경우

        userinfo = { # userInfo과 preference로 나눈이유 - preference가 foreignkey로 참조하기 때문에 나눠서 저장
            "userName":  data.get("userName"),
            "userEmail": data.get("userEmail"),
            "userId": data.get("userId"),
            "userPassword": bcrypt.hashpw(data.get("userPassword").encode('UTF-8'), bcrypt.gensalt()).decode('UTF-8'),
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

# @csrf_exempt
# def checkid(request):
# 아이디 중복체크를 하는 두가지 방벙
# 첫번째는 3S1S 처럼 프론트에서 중복체크 버튼을 하나 만들고, 기능을 만들어서 회원가입시에 두개의 id와 checkid를 비교해서 중복체크 여부 확인
# 두번째는 회원가입 기능 코드 안에서 모두 처리 해버리는 경우
# 결국엔 값을 다 입력하고 전송을 누른 상태에서 잘못된 상황을 인지할 수 있다.


@csrf_exempt
def signin(request):
    if request.method == 'POST': # 메소드가 post로 넘어온 경우
        data = JSONParser().parse(request) # 로그인 화면에서 얻어온 값을 json형태로 저장

        if data.get('userId') == "" or data.get('userPassword') == "": # 아이디 비밀번호 중 입력값이 없는 경우
            return JsonResponse({'message' : '아이디 또는 비밀번호를 입력하세요.'}, status=400)

        if UserInfo.objects.filter(userId=data.get('userId')).exists(): # 아이디가 같은 것이 있는지 확인
            login_user = UserInfo.objects.get(userId=data.get('userId')) # 아이디가 같은것이 있으면, 객체로 저장

            if bcrypt.checkpw(data.get('userPassword').encode('UTF-8'), login_user.userPassword.encode('UTF-8')):
                request.session['user'] = login_user.userId # session에 유저의 아이디를 기억
                return JsonResponse({'message' : '로그인 성공'}, status=201) # 성공시 render를 통해 메인화면으로 이동

            return JsonResponse({'message' : '비밀번호를 확인해주세요.'}, status=400) # 오류문 출력 이후, 로그인페이지로 이동
        return JsonResponse({'message' : '존재하지 않는 아이디 입니다.'}, status=400) # 다시 로그인 페이지로 이동

    return JsonResponse({'message' : 'Error'}, status=400) # 나중에는 render로 페이지 이동을 시킬 예정


@csrf_exempt
def findid(request):
    if request.method == 'POST': # 메소드가 post로 넘어온 경우
        data = JSONParser().parse(request) # 넘어온 data를 json 형식으로 변환

        if data.get('userName') == "" or data.get('userEmail') == "": # 이름 또는 이메일이 빈 값으로 넘어온경우
            return JsonResponse({'message' : '이름 또는 이메일을 입력하세요'}, status=400) # 오류문 출력하고, 나중에 페이지 이동 구현
        # 같은 이름과 이메일을 가지고 여러개의 아이디를 만드는 경우도 고려해야 하는지
        if UserInfo.objects.filter(userName=data.get('userName')).exists(): # 입력받은 이름이 데이터베이스에 저장이 되어 있는 경우
            find_user = UserInfo.objects.get(userName=data.get('userName')) # 입력받은 이름으로 데이터베이스 오브젝트 추출

            if find_user.userEmail == data.get('userEmail'): # 추출된 객체의 이메일과 입력받은 이메일이 같은 경우
                return JsonResponse({'userId':find_user.userId}, status=201) # id를 알려주고, 나중에 페이지 이동 구현

            return JsonResponse({'message' : '이메일을 확인해주세요'}, status=400)
        return JsonResponse({'message' : '존재하지 않은 사용자입니다.'}, status=400)

    return JsonResponse({'message' : 'Error'}, status=400)

@csrf_exempt
def logout(request): # 로그아웃 실행시
    del request.session['user'] # 로그인 시 저장했던 session에서 pop을 해서 제거함
    return redirect('/') # 로그아웃시 초기페이지로 이동 나중에 다시 페이지 이동 설정


@csrf_exempt
def mypage(request): # 아니면 인자로 userId를 받아도 됨

    userId = request.session['user']  # 로그인 성공하면 session에 userId가 담기게 됨

    if request.method == 'GET': # 마이페이지에 데이터를 띄우기 위한 method
        userObj = UserInfo.objects.get(userId=userId) # userId로 userinfo 데이터베이스에 있는 object를 가져옴
        # print(userObj.preference.preferenceEat)
        userInformation = UserInfoSerializer(userObj) # 데이터 베이스의 값들을 JSON 형태로 변환해서 저장
        # print(userInformation.data['preference'])
        return JsonResponse(userInformation.data,  status =200)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)

        return

    elif request.method == 'DELETE':

        return
