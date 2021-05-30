# Generated by Django 2.2.20 on 2021-05-30 07:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('idea', '0002_idea_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='IdeaStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='idea',
            name='status',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='idea.IdeaStatus', verbose_name='Idea Status'),
        ),
    ]