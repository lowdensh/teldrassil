from django.db import models
from users.models import CustomUser


def format_datetime(datetime):
    return datetime.strftime('%Y-%m-%d %H:%M:%S')


class Post(models.Model):
    title = models.CharField(
        max_length=80,
        default='Untitled blog post'
    )
    author = models.ForeignKey(
        to=CustomUser,
        on_delete=models.CASCADE,
        related_name='posts'
    )
    date_published = models.DateTimeField(auto_now_add=True)
    date_edited = models.DateTimeField(
        auto_now=True,
        null=True,
    )
    content = models.TextField(
        max_length=2056,
        default='There should be some post content here, but I was empty and left as the default :('
    )

    @property
    def short_title(self):
        max_chars = 29
        if len(self.title) > max_chars:
            return self.title[:max_chars] + '...'
        return self.title

    def __str__(self):
        return (
            f'"{self.short_title}" '
            f'by {self.author} '
            f'on {format_datetime(self.date_published)}'
        )

    class Meta:
        ordering = ['-date_published', 'author', ]
