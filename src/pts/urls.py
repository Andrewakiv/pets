from django.urls import path
from . import views

app_name = 'pts'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('post/<slug:post_slug>/', views.list_view, name='list_view'),
    path('about/', views.about, name='about'),
    path('add_page/', views.add_page, name='add_page'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
]
