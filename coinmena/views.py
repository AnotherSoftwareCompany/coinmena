from django.http import JsonResponse
from rest_framework.mixins import CreateModelMixin, ListModelMixin
from rest_framework.viewsets import GenericViewSet

from coinmena.models import Price
from coinmena.serilaizer import PriceSerializer
from coinmena.tasks import fetch_all_coin_pairs


class APIViewSet(CreateModelMixin, ListModelMixin, GenericViewSet):

    queryset = Price.objects.prefetch_related('pair__base', 'pair__pair').all()
    serializer_class = PriceSerializer

    def list(self, request, *args, **kwargs):
        last_five = self.get_queryset().order_by('-created_at')[:5]

        return JsonResponse(self.get_serializer(instance=last_five, many=True).data, safe=False)

    def create(self, request, *args, **kwargs):
        fetch_all_coin_pairs.delay()
        return JsonResponse({'success': True})
