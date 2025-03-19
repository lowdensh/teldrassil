from django.db import models
from django.utils.translation import gettext_lazy as _
from users.models import CustomUser


def format_datetime(datetime):
  return datetime.strftime('%Y-%m-%d %H:%M:%S')


class Category(models.Model):
  name = models.CharField(
    max_length=32,
    unique=True,
  )

  def __str__(self):
    return self.name

  class Meta:
    ordering = ['name', ]
    verbose_name = _('category')
    verbose_name_plural = _('categories')


class Tag(models.Model):
  name = models.CharField(
    max_length=16,
    unique=True,
  )

  def __str__(self):
    return self.name

  class Meta:
    ordering = ['name', ]
    verbose_name = _('tag')
    verbose_name_plural = _('tags')


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
  date_published = models.DateTimeField(
    auto_now_add=True
  )
  date_edited = models.DateTimeField(
    auto_now=True,
    null=True,
  )
  slug = models.SlugField(
    default='',
    null=False,
  )
  category = models.ForeignKey(
    to=Category,
    blank=True,
    null=True,
    on_delete=models.SET_NULL,
    related_name='posts',
  )
  tags = models.ManyToManyField(
    to=Tag,
    blank=True,
    related_name='tags',
  )
  content = models.TextField(
    default='There should be some post content here, but I was empty and left as the default :('
  )

  @property
  def short_title(self):
    max_chars = 39
    if len(self.title) > max_chars:
      return self.title[:max_chars] + '...'
    return self.title

  @property
  def short_content(self):
    max_chars = 350
    if len(self.content) > max_chars:
      return self.content[:max_chars] + '...'
    return self.content

  @property
  def has_category(self):
    if self.category is None:
      return False
    return True

  @property
  def string_of_category(self):
    if self.category is None:
      return 'none! (yet?)'
    return self.category.name

  @property
  def tags_count(self):
    return self.tags.count()

  @property
  def list_of_tags(self):
    return self.tags.all()

  @property
  def string_of_tags(self):
    if self.tags_count == 0:
      return 'none! (yet?)'

    list_of_tags = self.list_of_tags
    string = list_of_tags[0].name

    if self.tags_count == 1:
      return string

    for tag in list_of_tags[1:]:
      string += f', {tag.name}'

    return string

  def __str__(self):
    return (
      f'"{self.short_title}" '
      f'by: {self.author} '
      f'on: {format_datetime(self.date_published)}'
    )

  class Meta:
    ordering = ['-date_published', 'author', ]
    verbose_name = _('post')
    verbose_name_plural = _('posties')
