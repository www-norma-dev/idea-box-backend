# Generated by Django 2.2.20 on 2021-04-27 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Idea',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.TextField()),
                ('description', models.TextField(blank=True, null=True)),
                ('files', models.FileField(blank=True, null=True, upload_to='idea')),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
