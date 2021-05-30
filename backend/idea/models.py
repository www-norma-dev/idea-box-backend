from django.db import models


class IdeaStatus(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Idea(models.Model):
    id = models.AutoField(primary_key=True)

    date = models.DateField(
        auto_now_add=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    title = models.TextField(
        null=False,
        blank=False
    )

    status = models.ForeignKey('IdeaStatus',
                               verbose_name='Idea Status',
                               on_delete=models.SET_NULL,
                               null=True,
                               blank=True)

    description = models.TextField(
        null=True,
        blank=True
    )
    files = models.FileField(
        upload_to='idea',
        null=True,
        blank=True,
    )
    email = models.EmailField(
        null=False,
        blank=False,
        default=""
    )
    app_url = models.URLField(
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.title
