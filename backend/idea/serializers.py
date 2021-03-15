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

class IdeaSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=True, allow_blank=False, max_length=150)
    description = serializers.CharField(required=False, allow_blank=True)

    def create(self, validated_data):
        return Idea.objects.create(**validated_data)

    class Meta:
            model = Idea
            fields = '__all__'