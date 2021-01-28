from django.db import models
from django.contrib import admin

# Create your models here.
class Songs(models.Model):
    name = models.CharField(max_length=25)
    author = models.CharField(max_length=40)
    album = models.CharField(max_length=40)
    cover = models.ImageField(upload_to="albumCover", height_field=None, width_field=None, max_length=None)
    music = models.FileField(upload_to="songs")

class SongsAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'album', "cover")
    list_filter = ('name', )
    search_fields = ['name', 'author']