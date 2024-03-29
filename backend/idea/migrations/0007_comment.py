# Generated by Django 2.2.20 on 2021-07-08 07:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('idea', '0006_auto_20210530_1004'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('email', models.EmailField(default='', max_length=254)),
                ('message', models.TextField(blank=True, null=True)),
                ('idea', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='idea.Idea')),
            ],
        ),
    ]
