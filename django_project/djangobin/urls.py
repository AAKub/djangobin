from django.urls import path, re_path
from django.contrib.auth import views as auth_views
from django.contrib.flatpages import views as flat_views
from django.contrib.sitemaps.views import sitemap
from . import views
from .sitemaps import SnippetSitemap, FlatPageSitemap

app_name = 'djangobin'

sitemaps = {
    'snippets': SnippetSitemap,
    'flatpages': FlatPageSitemap,
}

urlpatterns = [
    path('', views.index, name='index'),
    re_path('^user/(?P<username>[A-Za-z0-9]+)/$', views.profile, name='profile'),
    path('trending/', views.trending_snippets, name='trending_snippets'),
    re_path('^trending/(?P<language_slug>[\w]+)/', views.trending_snippets, name='trending_snippets'),
    re_path('^(?P<snippet_slug>[\d]+)/', views.snippet_detail, name='snippet_detail'),
    re_path('^tag/(?P<tag>[\w-]+)/', views.tag_list, name='tag_list'),
    re_path('^download/(?P<snippet_slug>[\d]+)/$', views.download_snippet, name='download_snippet'),
    re_path('^raw/(?P<snippet_slug>[\d]+)/$', views.raw_snippet, name='raw_snippet'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('userdetails/', views.user_details, name='user_details'),
    path('signup/', views.signup, name='signup'),
    #re_path(r"^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/", views.activate_account, name='activate'),
    path('settings/', views.settings, name='settings'),
    re_path('delete/(?P<snippet_slug>[\d]+)/$', views.delete_snippet, name='delete_snippet'),
    path('search/', views.search, name='search'),
    path('about/', flat_views.flatpage, {'url': '/about/'}, name='about'),
    path('eula/', flat_views.flatpage, {'url': '/eula/'}, name='eula'),
    path('sitemap.xml/', sitemap, {'sitemaps': sitemaps}, name='sitemap'),
]
