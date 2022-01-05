from rest_framework.serializers import ModelSerializer, SerializerMethodField

from coinmena.models import Price


class PriceSerializer(ModelSerializer):
    class Meta:
        model = Price
        fields = ['price', 'pair', 'created_at']

    pair = SerializerMethodField()

    def get_pair(self, obj):
        return f'{obj.pair.base}/{obj.pair.pair}'
