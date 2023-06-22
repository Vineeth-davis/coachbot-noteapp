from django.db import models
from django.contrib.auth.models import User

class Note(models.Model):
    TEXT = 'text'
    AUDIO = 'audio'
    VIDEO = 'video'
    NOTE_TYPES = [
        (TEXT, 'Text'),
        (AUDIO, 'Audio'),
        (VIDEO, 'Video'),
    ]

    title = models.CharField(max_length=255)
    content = models.TextField()
    note_type = models.CharField(max_length=10, choices=NOTE_TYPES)
    file = models.FileField(upload_to='notes/', null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
