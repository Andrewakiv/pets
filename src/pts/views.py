from django.shortcuts import render, get_object_or_404, redirect

from .forms import AddPostForm
from .models import Pts, Category, TagPost

menu = [
    {'title': "About", 'url_name': 'pts:about'},
    {'title': "Add page", 'url_name': 'pts:add_page'},
    {'title': "Contact", 'url_name': 'pts:contact'},
    {'title': "Login", 'url_name': 'pts:login'}
]


def home(request):
    posts = Pts.published.all().select_related('category')
    data = {
        'posts': posts,
        'title': 'Home',
        'menu': menu,
        'cat_selected': 0
    }
    return render(request, 'pts/index.html', context=data)


def post_view(request, post_slug):
    post = get_object_or_404(Pts, slug=post_slug)
    tags = post.tags.all()
    data = {
        'post': post,
        'tags': tags,
        'title': post.title,
        'menu': menu,
        'cat_selected': 0
    }
    return render(request, 'pts/post.html', context=data)


def category_view(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    posts = Pts.published.filter(category_id=category.pk).select_related('category')
    data = {
        'posts': posts,
        'title': category.name,
        'menu': menu,
        'cat_selected': category.id
    }
    return render(request, 'pts/index.html', context=data)


def tag_view(request, tag_slug):
    tag = get_object_or_404(TagPost, slug=tag_slug)
    posts = tag.tags.filter(is_published=Pts.Status.PUBLISHED).select_related('category')  # tags = ...(related_name=tags)
    data = {
        'posts': posts,
        'title': tag.tag,
        'menu': menu,
        'cat_selected': None
    }
    return render(request, 'pts/index.html', context=data)


def about(request):
    data = {
        'title': 'About',
        'menu': menu,
    }
    return render(request, 'pts/index.html', context=data)


def add_page(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddPostForm()

    data = {
        'title': 'Add page',
        'menu': menu,
        'form': form
    }
    return render(request, 'pts/add_page.html', context=data)


def contact(request):
    data = {
        'title': 'Contact',
        'menu': menu,
    }
    return render(request, 'pts/index.html', context=data)


def login(request):
    data = {
        'title': 'Login',
        'menu': menu,
    }
    return render(request, 'pts/index.html', context=data)