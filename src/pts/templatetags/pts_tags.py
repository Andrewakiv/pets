from django import template
from django.db.models import Count

from pts.models import Category, TagPost

register = template.Library()


@register.inclusion_tag("pts/category.html")
def categories_tag(cat_selected=0):
    categories = Category.objects.annotate(total=Count('cats')).filter(total__gt=0)
    return {'categories': categories, 'cat_selected': cat_selected}


@register.inclusion_tag("pts/tags.html")
def tags_tag():
    tags = TagPost.objects.annotate(total=Count('tags')).filter(total__gt=0)
    return {'tags': tags}
