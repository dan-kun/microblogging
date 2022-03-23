from django.db import models
from django.utils import timezone


class Publication(models.Model):
    title = models.CharField(
        verbose_name="title",
        max_length=255,
        default=""
    )
    author = models.CharField(
        verbose_name="author",
        max_length=100,
        default=""
    )
    content = models.TextField(
        verbose_name="content",
        default=""
    )
    date = models.DateTimeField(
        verbose_name="date",
        default=timezone.now
    )
    up_votes = models.IntegerField(
        verbose_name="Upvotes",
        default=0
    )
    down_votes = models.IntegerField(
        verbose_name="Downvotes",
        default=0
    )

    @property
    def votes_rate(self):
        return self.up_votes - self.down_votes

    def short_content(self):
        return f"{self.content[0:50]}..."
