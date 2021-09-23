from django.contrib import admin

from .models import Idea, IdeaStatus, Blog


admin.site.register(Idea)
admin.site.register(IdeaStatus)
admin.site.register(Blog)