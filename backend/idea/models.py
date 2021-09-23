from django.db import models


class Blog(models.Model):
    id = models.AutoField(primary_key=True)

    description = models.TextField(
        null=True,
        blank=True
    )
    files = models.FileField(
        upload_to='blog',
        null=True,
        blank=True,
    )
    # separate with ;
    tags = models.TextField(
        null=False,
        blank=False
    )
    title = models.TextField(
        null=False,
        blank=False
    )

    content = models.TextField(
        null=False,
        blank=False
    )
    api_url = models.URLField(
        null=True,
        blank=True,
    )


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

    likes = models.IntegerField(
        null=False,
        default=0,
        blank=True
    )

    @property
    def avatar(self):
        return self.email[0].upper() if self.email else ""

    def __str__(self):
        return self.title


class Comment(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    email = models.EmailField(
        null=False,
        blank=False,
        default=""
    )

    message = models.TextField(
        null=True,
        blank=True
    )

    idea = models.ForeignKey(Idea, on_delete=models.CASCADE)
