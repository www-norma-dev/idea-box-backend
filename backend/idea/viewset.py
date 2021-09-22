from rest_framework import viewsets
from . import models
from . import serializers
from rest_framework import generics


class IdeaViewset(viewsets.ModelViewSet):
    queryset = models.Idea.objects.all()
    serializer_class = serializers.IdeaSerializer


class BlogViewset(viewsets.ModelViewSet):
    queryset = models.Blog.objects.all()
    serializer_class = serializers.BlogSerializer


class IdeaStatusViewset(viewsets.ModelViewSet):
    queryset = models.IdeaStatus.objects.all()
    serializer_class = serializers.IdeaStatusSerializer


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CommentSerializer
    queryset = models.Comment.objects.all()


class CommentList(generics.ListAPIView):
    serializer_class = serializers.CommentSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = models.Comment.objects.all()
        idea = self.kwargs['idea']
        if idea is not None:
            queryset = queryset.filter(idea_id=idea)

        return queryset
