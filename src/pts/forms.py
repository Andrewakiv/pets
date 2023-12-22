from django import forms
from .models import Category, Pts
from django.utils.text import slugify


class AddPostForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all(), required=False)

    class Meta:
        model = Pts
        fields = ['title', 'content', 'photo', 'is_published', 'category']
        widget = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.TextInput(attrs={'cols': 50, 'rows': 5})
        }
        labels = {'content': 'description'}

    def save(self, commit=True):
        instance = super(AddPostForm, self).save(commit=False)
        instance.slug = slugify(instance.title)

        if commit:
            instance.save()
        return instance
