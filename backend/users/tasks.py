from django.core import management

from ideabox_backend import celery_app


@celery_app.task
def clearsessions():
    management.call_command('clearsessions')
