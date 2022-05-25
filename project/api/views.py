from django.shortcuts import render
from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from .models import Paybylink, Dp, Card
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
    return Response(serializer.data)


@api_view(['POST'])
def card_create(request):
    serializer = CardSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def dp_create(request):
    serializer = DpSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


def convert_list(lst=list):
    nw_list = list()
    for x in lst:
        tp = (x, x)
        nw_list.append(tp)
    return nw_list

import requests
from django.conf import settings


class CurrencyExchangeService:
    def get_rates_from_api(self, base_currency):
        url = f'{settings.CURRENCY_RATES_URL}?base={base_currency}'
        return requests.get(url).json()

    def get_rate(self, base_currency, currency):
        return self.get_rates_from_api(base_currency)['rates'][currency]

    def convert(self, amount, currency, base_currency):
        if base.upper() == convert_currency.upper():
            return amount
        return round(float(amount) * float(self.get_rate(base.upper(), convert_currency.upper())), 3)