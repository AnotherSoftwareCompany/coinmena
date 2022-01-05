from django.db import models


class Coin(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    symbol = models.CharField(max_length=5, null=False, blank=False)

    def __str__(self):
        return self.symbol

class CoinPair(models.Model):
    base = models.ForeignKey(Coin, on_delete=models.CASCADE, related_name='base_prices')
    pair = models.ForeignKey(Coin, on_delete=models.CASCADE, related_name='pair_prices')


class Price(models.Model):
    pair = models.ForeignKey(CoinPair, on_delete=models.CASCADE)
    price = models.DecimalField(decimal_places=2, max_digits=12, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)




