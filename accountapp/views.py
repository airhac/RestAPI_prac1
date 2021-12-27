from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

#django 방법
# def hello_world(request):
#     return HttpResponse('Hello World!!')
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view()
def hello_world(request):
    return Response({"message": "Hello, world!"})