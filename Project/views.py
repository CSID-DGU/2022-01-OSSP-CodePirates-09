from django.shortcuts import render
from rest_framework.views import APIView


class Main(APIView):
    def get(self, request):
        # print("call by GET")
        return render(request, 'Project/main.html')

    def post(self, request):
        # print("call by POST")
        return render(request, 'Project/main.html')
