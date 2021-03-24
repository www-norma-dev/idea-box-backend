from django.conf.urls import include, url  # noqa
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import include, path
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view
from idea import views
import django_js_reverse.views

router = routers.DefaultRouter()
schema_view = get_swagger_view(title='idea-box-backend')

urlpatterns = [
    path('swagger/', schema_view),
    path('', include(router.urls)),
    path('', include('idea.urls')),
    path("admin/", admin.site.urls, name="admin"),
    path("jsreverse/", django_js_reverse.views.urls_js, name="js_reverse"),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]