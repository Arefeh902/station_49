# Generated by Django 2.1.9 on 2021-08-07 18:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0005_song_datetime'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='title',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='song',
            old_name='song_name',
            new_name='name',
        ),
    ]
