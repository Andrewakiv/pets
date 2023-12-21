from django.contrib import admin, messages

from .models import Pts, Category, Passport, TagPost


class PassportFilter(admin.SimpleListFilter):
    title = 'Passport status'
    parameter_name = 'status'

    def lookups(self, request, model_admin):
        return [
            ('available', 'available'),
            ('not_available', 'not available')
        ]

    def queryset(self, request, queryset):
        if self.value() == 'available':
            return queryset.filter(passport__isnull=False)
        elif self.value() == 'not_available':
            return queryset.filter(passport__isnull=True)


@admin.register(Pts)
class PtsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content', 'publish_date', 'updated_date', 'is_published', 'category']
    list_display_links = ['id', 'title']
    ordering = ['-publish_date', 'title']
    actions = ['set_to_published', 'set_to_draft']
    search_fields = ['is_published', 'category__name']
    list_filter = [PassportFilter, 'is_published', 'category__name']
    # list_editable = ('is_published',)

    @admin.action(description='Set status to Published')
    def set_to_published(self, request, queryset):
        count = queryset.update(is_published=Pts.Status.PUBLISHED)
        self.message_user(request, f'Have been changed status of {count} posts to Published')

    @admin.action(description='Set status to NotPublished')
    def set_to_draft(self, request, queryset):
        count = queryset.update(is_published=Pts.Status.DRAFT)
        self.message_user(request, f'Have been changed status of {count} posts to NotPublished',
                          messages.WARNING)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']


admin.site.register(Passport)
admin.site.register(TagPost)
