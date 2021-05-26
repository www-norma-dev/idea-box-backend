from django.db import models
from import_export.admin import ImportExportModelAdmin
from datetime import date

from taggit.managers import TaggableManager


class Idea(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.TextField(
        null=False,
        blank=False
    )
    description = models.TextField(
        null=True,
        blank=True
    )
    files = models.FileField(
        upload_to='idea',
        null=True,
        blank=True,
    )
    date = models.DateField(
        auto_now_add=True,
    )
    tags = TaggableManager()

    def get_tags(self):
        """ names() is a django-taggit method, returning a ValuesListQuerySet
        (basically just an iterable) containing the name of each tag as a string
        """
        return self.tags.names()

    def __str__(self):
        return self.title

    def to_json(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'filepath': self.files,
            'date': self.date,
            'tags': self.tags
        }