from . import models
from rest_framework import serializers

from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer
from drf_queryfields import QueryFieldsMixin
from dynamic_rest.serializers import DynamicModelSerializer, DynamicRelationField
from dynamic_rest.viewsets import DynamicModelViewSet
from rest_framework import viewsets

class TagsField(serializers.Field):
    """ custom field to serialize/deserialize TaggableManager instances.
    """
    def to_representation(self, value):
        """ in drf this method is called to convert a custom datatype into a primitive,
        serializable datatype.

        In this context, value is a plain django queryset containing a list of strings.
        This queryset is obtained thanks to get_tags() method on the Task model.

        Drf is able to serialize a queryset, hence we simply return it without doing nothing.
        """
        return value

    def to_internal_value(self, data):
        """ this method is called to restore a primitive datatype into its internal
        python representation.

        This method should raise a serializers.ValidationError if the data is invalid.
        """
        return data


class TaskSerializer(serializers.ModelSerializer):
    tags = TagsField(source="get_tags")
    # variables = VariableSerializer()

    def create(self, validated_data):
        # using "source=get_tags" drf "thinks" get_tags is a real field name, so the return value of
        # to_internal_value() is used a the value of a key called "get_tags" inside validated_data dict. We need to
        # remove it and handle the tags manually.
        tags = validated_data.pop("get_tags")
        task = models.Idea.objects.create(**validated_data)
        task.tags.add(*tags)

        return task

    class Meta:
        model = models.Idea
        # we exclude all those fields we simply receive from Socialminer
        # whenever we get a task or its status
        fields = [
                "title",
                "description",
                "date",
                "tags",
            ]


class IdeaSerializer(DynamicModelSerializer, QueryFieldsMixin, HyperlinkedModelSerializer):
    class Meta:
        model = models.Idea
        fields = ['title', 'tags']


class IdeaViewset(viewsets.ModelViewSet):
    queryset = models.Idea.objects.all()
    serializer_class = TaskSerializer
