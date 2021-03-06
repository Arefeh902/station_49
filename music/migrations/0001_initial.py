# Generated by Django 2.1.9 on 2021-08-02 10:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('song_name', models.CharField(max_length=300)),
                ('song_file', models.FileField(upload_to='songs')),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.Artist')),
            ],
        ),
    ]
