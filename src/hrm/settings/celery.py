import os
from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hrm.settings')

celery_app = Celery('hrm')

celery_app.config_from_object('django.conf:settings', namespace='CELERY')

celery_app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)