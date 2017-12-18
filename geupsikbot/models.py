from django.db import models
from django.utils import timezone
from datetime import datetime

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Menu(models.Model):
    id = models.AutoField(primary_key=True)
    date=models.DateTimeField(default=datetime.now().date())
    lunch = models.CharField(max_length=150, default="")
    dinner = models.CharField(max_length=150, default="")

