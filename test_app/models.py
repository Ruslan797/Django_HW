from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=120)  # VARCHAR
    description = models.TextField()
    author = models.CharField(max_length=100)
    published_date = models.DateField()

    def __str__(self):
        return f"Book '{self.title}'  -- Author '{self.author}'"


class Post(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    image_url = models.URLField(null=True, blank=True)


class UserProfile(models.Model):
    nickname = models.CharField(max_length=70, unique=True)
    bio = models.TextField(null=True, blank=True)
    website = models.URLField(max_length=250, null=True, blank=True)
    age = models.PositiveSmallIntegerField(null=True, blank=True)
    followers_count = models.PositiveBigIntegerField(null=True, blank=True)
    posts_count = models.PositiveIntegerField(null=True, blank=True)
    comments_count = models.PositiveIntegerField(null=True, blank=True)
    engagement_rate = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"User - {self.nickname}."











