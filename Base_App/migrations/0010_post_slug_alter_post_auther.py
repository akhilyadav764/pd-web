# Generated by Django 5.0.7 on 2024-08-01 08:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Base_App', '0009_comment_subcomment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='auther',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Base_App.author'),
        ),
    ]
