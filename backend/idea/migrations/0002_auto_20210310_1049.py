# Generated by Django 2.2.19 on 2021-03-10 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('idea', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='idea',
            name='text',
        ),
        migrations.AddField(
            model_name='idea',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='idea',
            name='title',
            field=models.TextField(default='default'),
            preserve_default=False,
        ),
    ]