from django.contrib.auth.models import User
from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


class Person(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pfp = models.ImageField(upload_to='profile_pics')
    pfp_thumbnail = ImageSpecField(source='pfp',
                                   processors=[ResizeToFill(200, 200)],
                                   format='JPEG',
                                   options={'quality': 90})
    bio = models.TextField(max_length=400, blank=True, default="I'm just a kid and life is a nightmare")
