from django.db import models
from import_export.admin import ImportExportModelAdmin

# Create your models here.
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

    def __str__(self):
        return (self.title + ":" + self.description)

    def to_json(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'filepath': str(self.files),
        }