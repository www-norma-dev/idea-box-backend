from django.conf.urls import include, url  # noqa
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import include, path
from rest_framework import routers
from idea import views

import django_js_reverse.views


router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('', include('idea.urls')),
    path("admin/", admin.site.urls, name="admin"),
    path("jsreverse/", django_js_reverse.views.urls_js, name="js_reverse"),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]