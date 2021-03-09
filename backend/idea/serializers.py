from django.contrib.auth.models import User, Group
from rest_framework import serializers
from idea.models import Idea


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class IdeaSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)
    text = serializers.CharField(required=True, allow_blank=True, max_length=100)

    class Meta:
            model = Idea
            fields = '__all__'