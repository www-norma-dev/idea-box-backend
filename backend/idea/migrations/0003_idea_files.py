# Generated by Django 2.2.19 on 2021-03-10 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('idea', '0002_auto_20210310_1049'),
    ]

    operations = [
        migrations.AddField(
            model_name='idea',
            name='files',
            field=models.FileField(blank=True, upload_to='idea'),
        ),
    ]