# Generated by Django 2.1.9 on 2021-08-05 17:14

from django.db import migrations, models
import music.models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_auto_20210805_1603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to=music.models.category_cover_upload_location),
        ),
        migrations.AlterField(
            model_name='category',
            name='icon',
            field=models.ImageField(blank=True, null=True, upload_to=music.models.category_icon_upload_location),
        ),
    ]