from django.core.management.base import BaseCommand, CommandError

from coinmena.models import CoinPair, Coin


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        parser.add_argument('base', type=str)
        parser.add_argument('pair', type=str)

    def handle(self, *args, **options):
        base = self.get_coin_if_exists(options['base'])
        pair = self.get_coin_if_exists(options['pair'])
        CoinPair.objects.create(
            base=base,
            pair=pair,
        )


    def get_coin_if_exists(self, symbol):
        coin =  Coin.objects.filter(symbol=symbol)
        if coin.exists():
            coin = coin.first()
        else:
            raise CommandError('Cint "%s" does not exist' % symbol)

        return coin
