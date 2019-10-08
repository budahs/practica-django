from django.db import models
from django.contrib.auth.models import User


class Article(models.Model):
    DRAFT = 'DRF'
    PUBLISHED = 'PUB'

    STATE = [
        [DRAFT, 'Draft'],
        [PUBLISHED, 'Published']
    ]

    title = models.CharField(max_length=150);
    introduction = models.TextField(null=True, blank=True)
    body = models.TimeField(null=True, blank=True)
    url = models.URLField()
    creation_date = models.DateTimeField(auto_now_add=True)
    modification_date = models.DateTimeField(auto_now=True)
    state =  models.CharField(max_length=3, choices=STATE, default=DRAFT)
    author = models.ForeignKey(User, related_name='photos', on_delete=models.CASCADE)

    def __str__(self):
        return self.title