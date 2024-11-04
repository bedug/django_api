from django.db import models


# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=50, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Album(models.Model):
    title = models.CharField(max_length=100)
    release_date = models.DateField()
    artist = models.ForeignKey(Artist, related_name="albums", on_delete=models.CASCADE)
    cover_image = models.ImageField(upload_to="album_covers/", blank=True, null=True)

    def __str__(self):
        return self.title


class Song(models.Model):
    title = models.CharField(max_length=100)
    album = models.ForeignKey(Album, related_name="songs", on_delete=models.CASCADE)
    audio_file = models.FileField(upload_to="songs/")
    duration = models.DurationField(blank=True, null=True)

    def __str__(self):
        return self.title
