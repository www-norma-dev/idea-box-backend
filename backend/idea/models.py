from django.db import models
from import_export.admin import ImportExportModelAdmin
from datetime import date


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
    date = models.DateField(
        auto_now_add=True,
    )
    email = models.EmailField(
        null=False,
        blank=False,
        default=""
    )

    def __str__(self):
        return self.title

    def to_json(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'filepath': self.files,
            'date': self.date,
        }
