from django.db import models
from django.utils import timezone
# from django.db.models.functions import Now

class Post(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    # publish = models.DateTimeField(db_default=Now())          # Django 5 feature: uses the database server’s current date and time as the default
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-publish']

    def __str__(self):
        return self.title