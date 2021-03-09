from django.db import models
from import_export.admin import ImportExportModelAdmin

# Create your models here.
class Idea(models.Model):
    id = models.AutoField(primary_key=True)
    text = models.TextField(
        null=True,
        blank=True
    )

    def __str__(self):
        return self.text

    def to_json(self):
        return {
            'text': self.text,
        }