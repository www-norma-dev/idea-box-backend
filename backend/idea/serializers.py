from django.contrib.auth.models import User, Group
from rest_framework import serializers
from idea.models import Idea, IdeaStatus


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class IdeaSerializer(serializers.ModelSerializer):
    status_name = serializers.CharField(source='status.name', required=False, read_only=True)
    avatar_name = serializers.CharField(source='avatar', required=False, read_only=True)

    class Meta:
        model = Idea
        fields = '__all__'


class IdeaStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = IdeaStatus
        fields = '__all__'
