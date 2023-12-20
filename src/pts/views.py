from django.shortcuts import render, get_object_or_404

from .models import Pts

menu = [
    {'title': "About", 'url_name': 'pts:about'},
    {'title': "Add page", 'url_name': 'pts:add_page'},
    {'title': "Contact", 'url_name': 'pts:contact'},
    {'title': "Login", 'url_name': 'pts:login'}
]


def home(request):
    posts = Pts.published.all()
    data = {
        'posts': posts,
        'title': 'Home',
        'menu': menu,
        'cat_selected': 0
    }
    return render(request, 'pts/index.html', context=data)


def list_view(request, post_slug):
    post = get_object_or_404(Pts, slug=post_slug)
    data = {
        'post': post,
        'title': post.title,
        'menu': menu,
        'cat_selected': 0
    }
    return render(request, 'pts/post.html', context=data)


def about(request):
    data = {
        'title': 'About',
        'menu': menu,
    }
    return render(request, 'pts/index.html', context=data)


def add_page(request):
    data = {
        'title': 'Add page',
        'menu': menu,
    }
    return render(request, 'pts/index.html', context=data)


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