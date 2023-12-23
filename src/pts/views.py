from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, FormView, UpdateView

from .forms import AddPostForm
from .models import Pts, Category, TagPost

menu = [
    {'title': "About", 'url_name': 'pts:about'},
    {'title': "Add page", 'url_name': 'pts:add_page'},
    {'title': "Contact", 'url_name': 'pts:contact'},
    {'title': "Login", 'url_name': 'pts:login'}
]


# def home(request):
#     posts = Pts.published.all().select_related('category')
#     data = {
#         'posts': posts,
#         'title': 'Home',
#         'menu': menu,
#         'cat_selected': 0
#     }
#     return render(request, 'pts/index.html', context=data)

class HomeListView(ListView):
    model = Pts
    template_name = 'pts/index.html'
    context_object_name = 'posts'
    paginate_by = 4

    def get_queryset(self):
        return Pts.published.all().select_related('category')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home'
        context['menu'] = menu
        context['cat_selected'] = 0
        return context

# class HomeView(TemplateView):
#     template_name = "pts/index.html"
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["posts"] = Pts.published.all().select_related('category')
#         context['title'] = 'Home'
#         context['menu'] = menu
#         context['cat_selected'] = 0
#         return context


# def post_view(request, post_slug):
#     post = get_object_or_404(Pts, slug=post_slug)
#     tags = post.tags.all()
#     data = {
#         'post': post,
#         'tags': tags,
#         'title': post.title,
#         'menu': menu,
#         'cat_selected': 0
#     }
#     return render(request, 'pts/post.html', context=data)


class PostDetailView(DetailView):
    # model = Pts
    template_name = 'pts/post.html'
    context_object_name = 'post'
    slug_url_kwarg = 'post_slug'  # from url

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['post'].title
        context['menu'] = menu
        context['cat_selected'] = None
        return context

    def get_object(self, queryset=None):
        return get_object_or_404(Pts.published, slug=self.kwargs[self.slug_url_kwarg])


# def category_view(request, category_slug):
#     category = get_object_or_404(Category, slug=category_slug)
#     posts = Pts.published.filter(category_id=category.pk).select_related('category')
#     data = {
#         'posts': posts,
#         'title': category.name,
#         'menu': menu,
#         'cat_selected': category.id
#     }
#     return render(request, 'pts/index.html', context=data)


class CategoryListView(ListView):
    model = Category
    template_name = 'pts/index.html'
    context_object_name = 'posts'  # for tag in template, default object_list
    allow_empty = False  # for 404 if have no items in posts
    paginate_by = 4

    def get_queryset(self):
        # category_slug from its url
        return Pts.published.filter(category__slug=self.kwargs['category_slug']).select_related('category')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = context['posts'].first().category  # from queryset first item then its category
        context['title'] = 'Category - '+category.name  # name from category
        context['menu'] = menu
        context['cat_selected'] = category.pk  # id from category
        return context


# def tag_view(request, tag_slug):
#     tag = get_object_or_404(TagPost, slug=tag_slug)
#     posts = tag.tags.filter(is_published=Pts.Status.PUBLISHED).select_related('category')  # tags = ...(related_name=tags)
#     data = {
#         'posts': posts,
#         'title': tag.tag,
#         'menu': menu,
#         'cat_selected': None
#     }
#     return render(request, 'pts/index.html', context=data)


class TagListView(ListView):
    model = TagPost
    template_name = 'pts/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        # category_slug from its url
        tag = get_object_or_404(TagPost, slug=self.kwargs['tag_slug'])
        return tag.tags.filter(is_published=Pts.Status.PUBLISHED).select_related('category')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tag = get_object_or_404(TagPost, slug=self.kwargs['tag_slug'])
        context['title'] = tag.tag
        context['menu'] = menu
        context['cat_selected'] = None
        return context


def about(request):
    data = {
        'title': 'About',
        'menu': menu,
    }
    return render(request, 'pts/index.html', context=data)


# def add_page(request):
#     if request.method == 'POST':
#         form = AddPostForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     else:
#         form = AddPostForm()
#
#     data = {
#         'title': 'Add page',
#         'menu': menu,
#         'form': form
#     }
#     return render(request, 'pts/add_page.html', context=data)


class AddPageView(FormView):
    template_name = "pts/add_page.html"
    form_class = AddPostForm
    success_url = reverse_lazy('pts:home')

    # we can realize the same without via CreateView
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Add page'
        context['menu'] = menu
        return context


class PostUpdateView(UpdateView):
    model = Pts
    fields = ['title', 'content', 'photo', 'is_published', 'category']
    template_name = "pts/add_page.html"
    success_url = reverse_lazy('pts:home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edit page'
        context['menu'] = menu
        return context


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