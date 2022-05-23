from rest_framework import serializers
from .models import Paybylink, Dp, Card


class PaybylinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paybylink
        fields = '__all__'


class DpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dp
        fields = '__all__'


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = '__all__'


class ConnectSerializer(serializers.Serializer):
    pay_by_link = PaybylinkSerializer(many=True)
    dp = DpSerializer(many=True)
    card = CardSerializer(many=True)

