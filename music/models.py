from datetime import timedelta

from django.db import models
from django.db.models.signals import post_save
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone


def song_icon_upload_location(instance, filename):
    return "song/%s_icon_%s" % (instance.name, filename)


def song_cover_upload_location(instance, filename):
    return "song/%s_cover_%s" % (instance.name, filename)


def song_file_upload_location(instance, filename):
    return "song/%s_file_%s" % (instance.name, filename)


def category_icon_upload_location(instance, filename):
    return "category/%s_icon_%s" % (instance.name, filename)


def category_cover_upload_location(instance, filename):
    return "category/%s_cover_%s" % (instance.name, filename)


class Artist(models.Model):
    django_user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user_profile", blank=True,
                                       null=True)
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=300)
    icon = models.ImageField(upload_to=category_icon_upload_location,
                             null=True,
                             blank=True)
    cover = models.ImageField(upload_to=category_cover_upload_location,
                              null=True,
                              blank=True)

    def __str__(self):
        return self.name


class Producer(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name


class Song(models.Model):
    datetime = models.DateTimeField(auto_now=True)
    duration = models.DurationField(default=timedelta(minutes=1))
    producers = models.ManyToManyField(Producer)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    name = models.CharField(max_length=300)
    song_file = models.FileField(upload_to='songs')
    icon = models.ImageField(upload_to=song_icon_upload_location,
                             null=True,
                             blank=True)
    cover = models.ImageField(upload_to=song_cover_upload_location,
                              null=True,
                              blank=True)

    def __str__(self):
        return self.name + ' - ' + str(self.artist)
