from .environ import env


CELERY_BROKER_URL=env.str('CELERY_BROKER_URL')
