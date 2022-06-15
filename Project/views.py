from django.shortcuts import render
from rest_framework.views import APIView


class Default(APIView):
    def get(self, request):
        return render(request, 'Project/default.html')

    def post(self, request):
        return render(request, 'Project/default.html')


def main(request):
    if request.method == 'GET':
        return render(request, 'Project/main.html')


def default(request):
    if request.method == 'GET':
        return render(request, 'Project/default.html')


def signin(request):
    if request.method == 'GET':
        return render(request, 'Project/signin.html')


def signup(request):
    if request.method == 'GET':
        return render(request, 'Project/signup.html')