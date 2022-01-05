from django.core.management.base import BaseCommand, CommandError

from coinmena.models import Coin


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        parser.add_argument('name', type=str)
        parser.add_argument('symbol', type=str)

    def handle(self, *args, **options):
        if Coin.objects.filter(symbol=options['symbol']).exists():
            print(f'Coin exists. "{options["symbol"]}"')
        else:
            Coin.objects.create(name=options["name"], symbol=options["symbol"])