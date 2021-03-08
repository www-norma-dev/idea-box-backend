web: gunicorn ideabox_backend.wsgi --chdir backend --limit-request-line 8188 --log-file -
worker: celery worker --workdir backend --app=ideabox_backend -B --loglevel=info
