from .models import Idea
from rest_framework import serializers, viewsets

from rest_framework.serializers import HyperlinkedModelSerializer
from drf_queryfields import QueryFieldsMixin
from dynamic_rest.serializers import DynamicModelSerializer
from taggit_serializer.serializers import (TagListSerializerField,
                                           TaggitSerializer)


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


# class TaskSerializer(serializers.ModelSerializer):
#     tags = TagsField(source="get_tags")
#
#     # variables = VariableSerializer()
#
#     def create(self, validated_data):
#         # using "source=get_tags" drf "thinks" get_tags is a real field name, so the return value of
#         # to_internal_value() is used a the value of a key called "get_tags" inside validated_data dict. We need to
#         # remove it and handle the tags manually.
#         tags = validated_data.pop("get_tags")
#         task = Idea.objects.create(**validated_data)
#         task.tags.add(*tags)
#
#         return task
#
#     class Meta:
#         model = Idea
#
#         fields = [
#             "title",
#             "description",
#             "date",
#             "tags",
#         ]


# class IdeaSerializer(DynamicModelSerializer, QueryFieldsMixin, HyperlinkedModelSerializer):
#     class Meta:
#         model = Idea
#         fields = ['title', 'tags']


class IdeaSerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField()

    # def create(self, validated_data):
    #     tags = validated_data.pop('tags')
    #     instance = super(IdeaSerializer, self).create(validated_data)
    #     instance.tags.set(*tags)
    #     return instance

    class Meta:
        model = Idea

        fields = '__all__'


class IdeaViewset(viewsets.ModelViewSet):
    queryset = Idea.objects.all().order_by('title')
    serializer_class = IdeaSerializer
