from django.shortcuts import render
from rest_framework.views import APIView


class Default(APIView):
    def get(self, request):
        return render(request, 'Project/signin.html') # 'Project/default.html'

    def post(self, request):
        return render(request, 'Project/default.html')
