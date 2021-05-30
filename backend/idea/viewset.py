from rest_framework import viewsets
from . import models
from . import serializers


class IdeaViewset(viewsets.ModelViewSet):
    queryset = models.Idea.objects.all()
    serializer_class = serializers.IdeaSerializer


class IdeaStatusViewset(viewsets.ModelViewSet):
    queryset = models.IdeaStatus.objects.all()
    serializer_class = serializers.IdeaStatusSerializer
