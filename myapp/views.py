import json
import uuid

from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import MyModel
from .serializers import MyModelSerializer

class SignUpView(generics.ListCreateAPIView):
    def get(self, request, *args, **kwargs):
        ret_dict = {
            "id":1,
            "email":request.GET.get("email","XXXX.EMAIL"),
        }
        # 处理 GET 请求的逻辑
        return HttpResponse(json.dumps(ret_dict))


class SignInView(generics.ListCreateAPIView):
    def get(self, request, *args, **kwargs):
        ret_dict = {
            "access_token":str(uuid.uuid1()),
            "refresh_token":str(uuid.uuid1()),
        }
        # 处理 GET 请求的逻辑
        return HttpResponse(json.dumps(ret_dict))


class Me(generics.ListCreateAPIView):
    def get(self, request, *args, **kwargs):
        ret_dict = {
            "id": 1,
            "email": request.GET.get("email", "XXXX.EMAIL"),
        }
        # 处理 GET 请求的逻辑
        return HttpResponse(json.dumps(ret_dict))