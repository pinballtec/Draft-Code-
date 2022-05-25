from django.shortcuts import render
from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from .models import Paybylink, Dp, Card
from rest_framework.exceptions import ValidationError
from .serializers import PaybylinkSerializer, CardSerializer, DpSerializer


# Create your views here.


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'Create': '/create/',
    }
    return Response(api_urls)


@api_view(['POST'])
def link_create(request):
    serializer = PaybylinkSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        raise ValidationError
    return Response(serializer.data)


@api_view(['POST'])
def card_create(request):
    serializer = CardSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        raise ValidationError
    return Response(serializer.data)


@api_view(['POST'])
def dp_create(request):
    serializer = DpSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        raise ValidationError
    return Response(serializer.data)

