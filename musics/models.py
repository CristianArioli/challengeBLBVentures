from django.db import models
from uuid import uuid4

# Create your models here.

class Musics(models.Model):
    id_music = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=255)
    path = models.CharField(max_length=255)