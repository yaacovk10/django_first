from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse

from django.shortcuts import render

# Create your views here.

@api_view(["GET", "POST"])
def index(req):
    return Response ('hello')

@api_view(["GET", "POST"])
def about(req):
    return Response ({"name":"yaacov", "age": 30})

@api_view(["GET", "POST"])
def list_users(req):
    return Response ('list_users')

@api_view(["GET", "POST"])
def game1(req):
    return Response ('game1')

@api_view(["GET", "POST"])
def game2(req):
    return Response ('game2')