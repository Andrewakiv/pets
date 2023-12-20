from django.db import models
from django.urls import reverse


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_published=Pts.Status.PUBLISHED)


class Pts(models.Model):
    class Status(models.IntegerChoices):
        DRAFT = 0, 'NotPublished'
        PUBLISHED = 1, 'Published'
    title = models.CharField(max_length=225)
    slug = models.SlugField(max_length=225, unique=True, db_index=True)
    content = models.TextField(blank=True)
    publish_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(choices=Status.choices, default=Status.PUBLISHED)

    objects = models.Manager()
    published = PublishedManager()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-publish_date']
        indexes = [
            models.Index(fields=['-publish_date']),
        ]

    def get_absolute_url(self):
        return reverse("pts:list_view", kwargs={"post_slug": self.slug})
