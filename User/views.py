from django.shortcuts import render
# from rest_framework.views import APIView
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
from django.views import View
from .models import UserInfo, UserPreference
from .serializers import UserInfoSerializer, UserPreferenceSerializer
from rest_framework.parsers import JSONParser
from django.shortcuts import render, redirect
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from openpyxl import load_workbook
from Project import views

import csv
import time
import re  # 정규 표현식을 지원
import json
import bcrypt  # 비밀번호 암호화를 위해서 패키지 다운로드
import pandas as pd # 크롤링하고 분석끝난 데이터 엑셀 파일을 가져오기 위한 import
import openpyxl # 엑셀 파일을 열고 데이터를 읽기


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
    response_data = {}
    if request.method == 'POST':
        data = {
            "userName": request.POST['userName'],
            "userEmail": request.POST['userEmail'],
            "userId": request.POST['userId'],
            "userPassword": request.POST['userPassword'],
            "userPasswordCheck": request.POST['userPasswordCheck'],
            "userPreferenceEat": request.POST['userPreferenceEat'],
            "userPreferenceDrink": request.POST['userPreferenceDrink'],
            "userPreferenceCafe": request.POST['userPreferenceCafe'],
            "userSex": request.POST['userSex'],
            "userAge": request.POST['userAge']
        }

        # data = JSONParser().parse(request)  # 넘어온 requset들을 Json 형태로 변환

        for key, val in data.items():  # json은 key-value 형태 이기 때문에 key,val값으로 for문 진행
            if val == "" and key:  # 만약 빈값으로 넘어온 밸류가 있다면 오류문 출력하고, 나중에 페이지 이동까지 구현
                return JsonResponse({'message': '입력되지 않은 항목이 있습니다.'}, status=400)  # 나중에 페이지 이동 구현

        # if data.get('userId') != data.get('userIdCheck'): # 프론트에서 중복체크 버트를 누르면 checkid 실행, 거기서 checkid가 확정
        #     return JsonResponse({'message': '아이디 중복체크를 하지 않았습니다.'}, status=400)

        if data.get('userPassword') != data.get('userPasswordCheck'):  # 프론트에서 구현 가능한건인가 ?, 일단 비밀번호 비교
            return JsonResponse({'message': '입력된 두 비밀번호가 다릅니다.'}, status=400)
        else:
            regex = re.compile(r"[a-zA-Z0-9_]+@[a-z]+[.][a-z.]+")  # 정규표현을 적어서 이메일 유효성 검사
            vaildEmail = regex.search(data.get('userEmail'))  # 입력받은 데이터를 정규표현에 대입하여 검사
            if vaildEmail == None:  # 이메일 형식이 유효하지 않는 경우
                return JsonResponse({'message': '이메일 형식이 올바르지 않습니다.'}, status=400)  # 나중에 페이지 이동으로 구현

        # 여기 까지 진행 되었다는 것은 빈값이 넘어온 것이 없고, 아이디 중복체크도 진행했고, 비밀번호도 알맞게 입력한 경우

        userinfo = {  # userInfo과 preference로 나눈이유 - preference가 foreignkey로 참조하기 때문에 나눠서 저장
            "userName": data.get("userName"),
            "userEmail": data.get("userEmail"),
            "userId": data.get("userId"),
            "userPassword": bcrypt.hashpw(data.get("userPassword").encode('UTF-8'), bcrypt.gensalt()).decode('UTF-8'),
            "userSex": data.get("userSex"),
            "userAge": data.get("userAge")
        }

        userinfo_serializer = UserInfoSerializer(data=userinfo)  # userinfo로 저장한 딕셔너리형태 db에 저장
        if userinfo_serializer.is_valid():
            userinfo_serializer.save()

            preference = {  # foreignkey로 참조한 자식테이블이기 때문에 나눠서 데이터 저장,
                # 그리고 userInfo가 선행되어서 저장되어야하기 때문에 if문으로 조건 진행
                "userId": data.get("userId"),
                "userPreferenceEat": data.get("userPreferenceEat"),
                "userPreferenceDrink": data.get("userPreferenceDrink"),
                "userPreferenceCafe": data.get("userPreferenceCafe")
            }

            prefer_serializer = UserPreferenceSerializer(data=preference)  # preference로 저장한 딕셔너리형태 db에 저장
            if prefer_serializer.is_valid():
                prefer_serializer.save()
                response_data['error'] = "회원가입이 완료되었습니다."
                return redirect(views.default)  # 두 테이블이 모두 저장되면 회원가입 성공 !
        return HttpResponse({"message : Error"}, status=400)  # 그렇지 않으면 실패


# @csrf_exempt
# def checkid(request):
# 아이디 중복체크를 하는 두가지 방벙
# 첫번째는 3S1S 처럼 프론트에서 중복체크 버튼을 하나 만들고, 기능을 만들어서 회원가입시에 두개의 id와 checkid를 비교해서 중복체크 여부 확인
# 두번째는 회원가입 기능 코드 안에서 모두 처리 해버리는 경우
# 결국엔 값을 다 입력하고 전송을 누른 상태에서 잘못된 상황을 인지할 수 있다.


@csrf_exempt
def signin(request):
    if request.method == 'POST':  # 메소드가 post로 넘어온 경우
        data = {
            "userId": request.POST['userId'],
            "userPassword": request.POST['userPassword']
        }

        # data = JSONParser().parse(request)  # 로그인 화면에서 얻어온 값을 json형태로 저장

        if data.get('userId') == "" or data.get('userPassword') == "":  # 아이디 비밀번호 중 입력값이 없는 경우
            return render(request, 'signin.html', {'message': '아이디 또는 비밀번호를 입력하세요.'}, status=400)

        if UserInfo.objects.filter(userId=data.get('userId')).exists():  # 아이디가 같은 것이 있는지 확인
            login_user = UserInfo.objects.get(userId=data.get('userId'))  # 아이디가 같은것이 있으면, 객체로 저장

            if bcrypt.checkpw(data.get('userPassword').encode('UTF-8'), login_user.userPassword.encode('UTF-8')):
                request.session['user'] = login_user.userId  # session에 유저의 아이디를 기억
                return redirect(views.main)  # 성공시 render를 통해 메인화면으로 이동

            return render(request, 'Project/signin.html', {'message': '비밀번호를 확인해주세요.'}, status=400)  # 오류문 출력 이후, 로그인페이지로 이동
        return render(request, 'Project/signin.html', {'message': '존재하지 않는 아이디 입니다.'}, status=400)  # 다시 로그인 페이지로 이동

    return render(request, 'Project/signin.html', {'message': 'Error'}, status=400)  # 나중에는 render로 페이지 이동을 시킬 예정


@csrf_exempt
def findid(request):
    if request.method == 'POST':  # 메소드가 post로 넘어온 경우
        data = {
            "userName": request.POST['userName'],
            "userEmail": request.POST['userEmail']
        }
        # data = JSONParser().parse(request)  # 넘어온 data를 json 형식으로 변환

        for key, val in data.items():  # json은 key-value 형태 이기 때문에 key,val값으로 for문 진행
            if val == "" and key:  # 만약 빈값으로 넘어온 밸류가 있다면 오류문 출력하고, 나중에 페이지 이동까지 구현
                return JsonResponse({'message': '입력되지 않은 항목이 있습니다.'}, status=400)  # 나중에 페이지 이동 구현

        # 같은 이름과 이메일을 가지고 여러개의 아이디를 만드는 경우도 고려해야 하는지
        if UserInfo.objects.filter(userName=data.get('userName')).exists():  # 입력받은 이름이 데이터베이스에 저장이 되어 있는 경우
            find_user = UserInfo.objects.get(userName=data.get('userName'))  # 입력받은 이름으로 데이터베이스 오브젝트 추출

            if find_user.userEmail == data.get('userEmail'):  # 추출된 객체의 이메일과 입력받은 이메일이 같은 경우
                return JsonResponse({'userId': find_user.userId}, status=201)  # id를 알려주고, 나중에 페이지 이동 구현

            return JsonResponse({'message': '이메일을 확인해주세요'}, status=400)
        return JsonResponse({'message': '존재하지 않은 사용자입니다.'}, status=400)

    return JsonResponse({'message': 'Error'}, status=400)


@csrf_exempt
def findpw(request):
    if request.method == 'POST':
        data = { # 나중에 form태그 순서 맞추기
            "userName":request.POST['userName'],
            "userEmail":request.POST['userEmail'],
            "userId":request.POST['userId']
        }
        # data = JSONParser().parse(request)


        for key, val in data.items():  # json은 key-value 형태 이기 때문에 key,val값으로 for문 진행
            if val == "" and key:  # 만약 빈값으로 넘어온 밸류가 있다면 오류문 출력하고, 나중에 페이지 이동까지 구현
                return JsonResponse({'message': '입력되지 않은 항목이 있습니다.'}, status=400)  # 나중에 페이지 이동 구현

        if UserInfo.objects.filter(userName=data.get('userName')).exists():  # 입력받은 이름이 데이터베이스에 저장이 되어 있는 경우
            find_user = UserInfo.objects.get(userName=data.get('userName'))  # 입력받은 이름으로 데이터베이스 오브젝트 추출

            if find_user.userEmail == data.get('userEmail'):  # 추출된 객체의 이메일과 입력받은 이메일이 같은 경우
                if find_user.userId == data.get('userId'):  # 추출된 객체의 아이디와 입력받은 아이디가 같은 경우

                    return JsonResponse({'userPassword': find_user.userPassword}, status=201)  # 추가로 변경가능하게만들지 고민중

                return JsonResponse({'message': '아이디를 확인하세요'}, status=400)
            return JsonResponse({'message': '이메일을 확인하세요.'}, status=400)
        return JsonResponse({'message': '이름을 확인하세요'}, status=400)
    return JsonResponse({'message': 'Error'}, status=400)


@csrf_exempt
def logout(request):  # 로그아웃 실행시
    del request.session['user']  # 로그인 시 저장했던 session에서 pop을 해서 제거함
    return redirect('/')  # 로그아웃시 초기페이지로 이동 나중에 다시 페이지 이동 설정


@csrf_exempt
def mypage(request):  # 아니면 인자로 userId를 받아도 됨

    userId = request.session['user']  # 로그인 성공하면 session에 userId가 담기게 됨

    if request.method == 'GET':  # 마이페이지에 데이터를 띄우기 위한 method
        userObj = UserInfo.objects.get(userId=userId)  # userId로 userinfo 데이터베이스에 있는 object를 가져옴
        preferenceObj = UserPreference.objects.get(userId=userId)  # userId로 userPreferenc 데이터베이스에 있는 object를 가져옴

        info_user = UserInfoSerializer(userObj)  # UserInfo 데이터 베이스의 값들을 JSON 형태로 변환해서 저장
        info_preference = UserPreferenceSerializer(preferenceObj)  # userPreference 데이터 베이스의 값들을 JSON 형태로 저장

        userInfomation = {  # userInfo, userPreference, userPartner DB 저장데이터들을 하나로 묶은 형태
            "user": info_user.data,
            "preference": info_preference.data,
        }
        # print(userInfomation.get('user'))  # 데이터를 받아서 출력하는 예시
        # example = userInfomation.get('user') # 데이터를 받아서 출력하는 예시
        # print(example.get('userName')) # 데이터를 받아서 출력하는 예시

        return JsonResponse(userInfomation, status=200)

    elif request.method == 'PUT':  # 모든 값들이 다 넘어온다는 걸 가정으로 구현, 값을 바꾸지 않아도 기존의 값을 넘긴다는 생각
        data = JSONParser().parse(request)  # 넘어온 값들을 Json으로 저장

        for key, val in data.items():  # json은 key-value 형태 이기 때문에 key,val값으로 for문 진행
            if val == "" and key:  # 만약 빈값으로 넘어온 밸류가 있다면 오류문 출력하고, 나중에 페이지 이동까지 구현
                return JsonResponse({'message': '입력되지 않은 항목이 있습니다.'}, status=400)  # 나중에 페이지 이동 구현

        Info_user = UserInfo.objects.get(userId=userId)  # DB에 저장되어 있는 userInfo 객체를 반환

        Info_user.userAge = data.get('userAge')  # 입력받은 userAge를 db에 수정
        Info_user.userImage = data.get('userImage')  # 입력받은 userImage, 나중에 유효성 검사 필요하면 진행, 아니면 따로 만들어서 진행

        regex = re.compile(r"[a-zA-Z0-9_]+@[a-z]+[.][a-z.]+")  # 정규표현을 적어서 이메일 유효성 검사
        vaildEmail = regex.search(data.get('userEmail'))  # 입력받은 데이터를 정규표현에 대입하여 검사
        if vaildEmail == None:  # 이메일 형식이 유효하지 않는 경우
            return JsonResponse({'message': '이메일 형식이 올바르지 않습니다.'}, status=400)  # 나중에 페이지 이동으로 구현
        else:
            Info_user.userEmail = data.get('userEmail')  # 유효성 검사를 통과 하면 DB 수정

        if data.get('userPassword') != data.get('userPasswordCheck'):  # 비밀번호 수정시 비밀번호가 틀리게 입력하는 경우
            return JsonResponse({'message': '입력한 비밀번호가 다릅니다.'}, status=400)
        elif data.get('userPassword') == data.get('userPasswordCheck'):  # 입력한 비밀번호가 같은 경우
            Info_user.userPassword = bcrypt.hashpw(data.get("userPassword").encode('UTF-8'), bcrypt.gensalt()).decode(
                'UTF-8')
            # bcrypt를 이용해서 DB에 저장

        Info_preference = UserPreference.objects.get(userId=userId)  # userId를 이용하여 사용자의 선호도 객체 반환
        Info_preference.preferenceEat = data.get('preferenceEat')  # 입력된 값으로 db 값 변경
        Info_preference.preferenceDrink = data.get('preferenceDrink')  # 입력된 값으로 db 값 변경
        Info_preference.preferenceCafe = data.get('preferenceCafe')  # 입력된 값으로 db 값 변경

        Info_user.save()  # 변경된 사항을 db에 반영하고 저장
        Info_preference.save()  # 변경된 사항을 db에 반영하고 저장

        return JsonResponse({'message': '회원정보가 수정되었습니다.'}, status=200)
    return JsonResponse({'message': 'Error'}, status=400)


@csrf_exempt
def deleteuser(request):
    if request.method == 'DELETE':  # method가 DELETE로 들어온 경우
        user = UserInfo.objects.get(userId=request.session['user'])  # userId로 객체 불러와서 저장
        user.delete()  # user 삭제 진행
        del request.session['user']  # 혹시 모르니 로그아웃 진행
        return JsonResponse({'message': '회원탈퇴가 완료되었습니다.'}, status=200)  # 나중에 페이지 구현완료되면 메인으로 이동


@csrf_exempt
def crawling(request):
    # if request.method == 'GET': # 일단 위치 주소 받아야하고, 카테고리 누른 거받아야 해서 get으로 설정
    location = "잠실역"  # 나중에는 입력받은 주소로 치환하기 request.get('location')
    category = "카페"  # 나중에는 입력받은 카테고리로 치환하기 request.get('categoey')로 변경
    purpose = ""  # 나중에는 입력받은 방문목적으로 치환하기
    # preference = UserPreference.objects.get(userId=request.session['user'])  # 세션에 저장된 userId 사용해서 선호도 객체반환
    mood = ""
    test1 = "preference."

    driver = webdriver.Chrome('/Users/munchanghyeon/opt/chromedriver')  # 나중에는 프로젝트 파일에 포함시키기
    url = "https://www.diningcode.com"  # 다이닝코드 url를 저장
    driver.get(url)  # url를 가져와서 다이닝코드로 접속

    driver.implicitly_wait(2)  # 웹사이트 로딩 될때까지 2초 기다림

    driver.find_element_by_css_selector('#div_popup > div > div:nth-child(3)').click()  # 팝업창 닫기

    search = driver.find_element_by_css_selector('#txt_keyword')  # 검색창 css 선택
    search.click()  # 입력을 위해 검색창 클릭

    search.send_keys(location) # 클릭된 검색창에 특정 단어 입력 //  나중에는 location으로 대체 //
    search.send_keys(Keys.ENTER)  # 입력을 완료하고 엔터키를 누름

    # 카테고리, 방문목적, 분위기 다 보기위해서 펼치기 버튼 클릭 첫번째는 카테고리, 두번째는 방문목적, 세번째는 분위기
    driver.find_element_by_css_selector(
        '#root > div > div > div.SearchFilter > div.FilterLine.CategoryFilter > button > div').click()
    driver.find_element_by_css_selector(
        '#root > div > div > div.SearchFilter > div:nth-child(7) > button > div').click()
    driver.find_element_by_css_selector(
        '#root > div > div > div.SearchFilter > div:nth-child(8) > button > div').click()

    # if문으로 카테고리 입력에 따라 클릭을 다르게 진행, 몇개 케이스가 없기 때문에 미리 진행
    if category == "술집":
        driver.find_element_by_xpath('//*[@id="root"]/div/div/div[1]/div[3]/ul/li[4]/div').click()
        preferenceCategory = "preferenceDrink"
    elif category == "밥집":
        driver.find_element_by_xpath('//*[@id="root"]/div/div/div[1]/div[3]/ul/li[2]/div').click()
        preferenceCategory = "preferenceEat"
    elif category == "카페":
        driver.find_element_by_xpath('//*[@id="root"]/div/div/div[1]/div[3]/ul/li[3]/div').click()
        preferenceCategory = "preferenceCafe"

    driver.implicitly_wait(2)

    if purpose == "점심식사":
        driver.find_element_by_xpath('//*[@id="root"]/div/div/div[1]/div[7]/ul/li[2]/div').click()
    elif purpose == "저녁식사":
        driver.find_element_by_xpath('//*[@id="root"]/div/div/div[1]/div[7]/ul/li[3]/div').click()
    elif purpose == "데이트":
        driver.find_element_by_xpath('//*[@id="root"]/div/div/div[1]/div[7]/ul/li[7]/div').click()
    elif purpose == "회식":
        driver.find_element_by_xpath('//*[@id="root"]/div/div/div[1]/div[7]/ul/li[8]/div').click()

    driver.implicitly_wait(2)

    if mood == "가성비좋은":
        driver.find_element_by_xpath('//*[@id="root"]/div/div/div[1]/div[8]/ul/li[1]/div').click()
    elif mood == "분위기좋은":
        driver.find_element_by_xpath('//*[@id="root"]/div/div/div[1]/div[8]/ul/li[2]/div').click()
    elif mood == "고급스러운":
        driver.find_element_by_xpath('//*[@id="root"]/div/div/div[1]/div[8]/ul/li[5]/div').click()
    elif mood == "시끌벅적한":
        driver.find_element_by_xpath('//*[@id="root"]/div/div/div[1]/div[8]/ul/li[7]/div').click()
    elif mood == "조용한":
        driver.find_element_by_xpath('//*[@id="root"]/div/div/div[1]/div[8]/ul/li[8]/div').click()
    elif mood == "깔끔한":
        driver.find_element_by_xpath('//*[@id="root"]/div/div/div[1]/div[8]/ul/li[9]/div').click()
    elif mood == "예쁜":
        driver.find_element_by_xpath('//*[@id="root"]/div/div/div[1]/div[8]/ul/li[12]/div').click()

    # 더보기 클릭해서 넘어가는 페이지 에서 크롤링 진행
    more_btn = driver.find_element_by_css_selector('#root > div > div > div.Body > div.RList > div > button')  # 결과 더보기
    more_btn.click()  # 클릭해서 진행

    driver.implicitly_wait(2)  # 웹사이트 로딩 될때까지 2초 기다림

    items = driver.find_elements_by_css_selector('.PoiBlock')  # 상품 정보를 모두 가지고 있는 div 태그 지정

    # f = open(r"/Users/munchanghyeon/PycharmProjects/2022-01-OSSP1-CodePirates-09/data.csv", 'w', encoding='utf-8')
    # csvWriter = csv.writer(f)

    for item in items:  # for문을 사용해서 상품 이름, 상품 주소를 출력
        name = item.find_element_by_css_selector('.InfoHeader > h2').get_attribute('innerText')  # .text가 안먹어서 설정
        address = item.find_element_by_css_selector('.Category > span').get_attribute('innerText')  # 나중에 카테고리도 출력
        try:
            review = item.find_element_by_css_selector('.Review').get_attribute('innerText')  # 리뷰 출력
        except:
            review = "리뷰가 없습니다."
        name = re.sub(r"[0-9.]", "", name)
        print("가게명 : " + name)
        print("가게 주소 : " + address)
        print("대표 리뷰 : " + review)
        print("######")
      #  csvWriter.writerow([name, address, review])

    # f.close()
    return 0  # 나중에는 이동할 페이지나 리턴 값 구현

@csrf_exempt
def createcourse(request):
    if request.method == 'GET':
        data = {
            "location": request.GET['location'], # 검색한 위치 받기
            "1stcategory": request.GET['1stcategory'], # 첫번째 카테고리 받기
            "2ndcategory": request.GET['2ndcategory'], # 두번째 카테고리 받기
            "3rdcategory": request.GET['3rdcategory'] # 세번쨰 카테고리 빋기
        }

        firstcourse = data.get('location') + "." + data.get('1stcategory') # 첫번째 코스 sheet 저장
        secondcourse = data.get('location') + "." + data.get('2ndcategory') # 두번째 코스 sheet 저장
        thirdcourse = data.get('location') + "." + data.get('3rdcategory') # 세번쨰 코스 sheet 저장

        filename = "data.xlsx" # 열기위한 파일명 저장
        xlxs = load_workbook(filename=filename) # 저장한 filename를 통해서 엑셀 파일 열기
        # xlxs = pd.read_excel(filename, sheet_name=firstcourse)

        onesheet = xlxs[firstcourse] # 첫번째 카테고리에 대한 시트명 저장
        twosheet = xlxs[secondcourse] # 두번째 카테고리에 대한 시트명 저장
        threesheet = xlxs[thirdcourse] # 세번쨰 카테고리에 대한 시트명 저장

        fincourse = [] # 최종 코스를 저장하기 위한 리스트

        # 이거 전체를 for문으로 감싸서 3번 반복하는 방법도 생각해볼것 !

        row = onesheet[2] # 가져올 열 번호 지정
        for cell in row:
            fincourse += [cell.value] # 추출된 데이터를 추가

        row = twosheet[16] # 가져올 열 번호 저장
        for cell in row:
            fincourse += [cell.value] # 추출된 데이터를 추가

        row = threesheet[8] # 가져올 열 번호 저장
        for cell in row:
            fincourse += [cell.value] # 추출된 데이터를 추가

        print(fincourse)
        print(onesheet['C1'].value) # 하나의 셀을 저장하는 방식
        context ={
            '1sttitle': fincourse[0],
            '1stloc':fincourse[1],
            '1streview':fincourse[2],
            '2ndtitle':fincourse[3],
            '2ndloc':fincourse[4],
            '2ndreview':fincourse[5],
            '3rdtitle':fincourse[6],
            '3rdloc':fincourse[7],
            '3rdreview':fincourse[8],
            'location' : data.get('location'),
            '1stcategory':data.get('1stcategory'),
            '2ndcategory':data.get('2ndcategory'),
            '3rdcategory':data.get('3rdcategory')
        }

        print(context)

        return render(request, 'Project/main1.html', {'context':context})


@csrf_exempt
def main(request):
    if request.method == 'GET':
        return redirect(views.main)

