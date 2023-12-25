from django.urls import path
from . import views

app_name = 'pts'

urlpatterns = [
    # path('home/', views.home, name='home'),
    path('home/', views.HomeListView.as_view(), name='home'),
    # path('post/<slug:post_slug>/', views.post_view, name='post_view'),
    path('post/<slug:post_slug>/', views.PostDetailView.as_view(), name='post_view'),
    path('about/', views.about, name='about'),
    # path('add_page/', views.add_page, name='add_page'),
    path('add_page/', views.AddPageView.as_view(), name='add_page'),
    path('edit_page/<slug:slug>/', views.PostUpdateView.as_view(), name='add_page'),
    path('contact/', views.contact, name='contact'),
    # path('login/', views.login, name='login'),
    # path('category/<slug:category_slug>/', views.category_view, name='category_view'),
    path('category/<slug:category_slug>/', views.CategoryListView.as_view(), name='category_view'),
    # path('tags/<slug:tag_slug>/', views.tag_view, name='tag_view'),
    path('tags/<slug:tag_slug>/', views.TagListView.as_view(), name='tag_view'),
]

