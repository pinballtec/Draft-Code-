from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from .models import Paybylink, Dp, Card
from .serializers import ConnectSerializer
# Create your views here.


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/task-list/',
        'Create': '/task-create/',
    }
    return Response(api_urls)


@api_view(['POST'])
def link_create(request):
    serializer = ConnectSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
