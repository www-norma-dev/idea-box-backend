from django.conf.urls import include, url  # noqa
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view
import django_js_reverse.views
from idea.viewset import IdeaViewset, IdeaStatusViewset, CommentViewSet, CommentList, BlogViewset
from django.conf.urls.static import static
from django.conf import settings

router = routers.DefaultRouter()
schema_view = get_swagger_view(title='idea-box-backend')

router.register('idea', IdeaViewset)
router.register('idea_status', IdeaStatusViewset)
router.register('blog',BlogViewset)
router.register('comment', CommentViewSet)

urlpatterns = [
                  path('swagger/', schema_view),
                  path('api/comments/<int:idea>/', CommentList.as_view()),
                  path('api/', include(router.urls)),
                  path("admin/", admin.site.urls, name="admin"),
                  path("jsreverse/", django_js_reverse.views.urls_js, name="js_reverse"),
                  path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
