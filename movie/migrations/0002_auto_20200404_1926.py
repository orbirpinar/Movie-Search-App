# Generated by Django 3.0.5 on 2020-04-04 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='name',
        ),
        migrations.AddField(
            model_name='movie',
            name='movie_id',
            field=models.IntegerField(default=123),
            preserve_default=False,
        ),
    ]
