from django.contrib.auth import get_user_model
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
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, null=True, default=None)
    publish_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(choices=Status.choices, default=Status.PUBLISHED)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, related_name='cats')
    tags = models.ManyToManyField('TagPost', blank=True, related_name='tags')
    passport = models.OneToOneField('Passport', on_delete=models.SET_NULL, null=True, blank=True,
                                    related_name='pass_id')
    author = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True, default=None,
                                    related_name='posts')
    owner = models.ForeignKey('Owner', on_delete=models.CASCADE, null=True, default=None,
                              related_name='owners')

    objects = models.Manager()
    published = PublishedManager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Pets'
        verbose_name_plural = 'Pets'
        ordering = ['-publish_date']
        indexes = [
            models.Index(fields=['-publish_date']),
        ]

    def get_absolute_url(self):
        return reverse("pts:post_view", kwargs={"post_slug": self.slug})


class Category(models.Model):
    name = models.CharField(max_length=225, db_index=True)
    slug = models.SlugField(max_length=225, db_index=True, unique=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("pts:category_view", kwargs={"category_slug": self.slug})


class TagPost(models.Model):
    tag = models.CharField(max_length=225, db_index=True)
    slug = models.SlugField(max_length=225, db_index=True, unique=True)

    def __str__(self):
        return self.tag

    def get_absolute_url(self):
        return reverse("pts:tag_view", kwargs={"tag_slug": self.slug})


class Passport(models.Model):
    passport_id = models.IntegerField(null=True)

    def __str__(self):
        return str(self.passport_id)


class Owner(models.Model):
    name = models.CharField(max_length=225, db_index=True)
    slug = models.SlugField(max_length=225, db_index=True, unique=True)

    class Meta:
        verbose_name = 'Owner'
        verbose_name_plural = 'Owners'

    def __str__(self):
        return self.name
