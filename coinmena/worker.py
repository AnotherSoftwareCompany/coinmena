import os
from celery import Celery

from coinmena import settings


HOUR = 60 * 60


from django.conf import settings

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'coinmena.settings')

# Using a string here means the worker will not have to
# pickle the object when using Windows.


CELERY_TASKS = {
    "fetch_hourly_rate": {
        "task": "fetch_all_coin_pairs",
        "schedule": HOUR
    },
}
celery_app = Celery(
    "coinmena", broker=settings.REDIS_URL, include=["coinmena.tasks"]
)

celery_app.config_from_object('django.conf:settings')
celery_app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
celery_app.conf.beat_schedule = CELERY_TASKS


