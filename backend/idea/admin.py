from django.contrib import admin

from .models import Idea, IdeaStatus


admin.site.register(Idea)
admin.site.register(IdeaStatus)
