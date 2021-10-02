from django.contrib import admin
from django.urls import path

from articles import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', views.archive, name="archive"),
    path(r'^article/(?P<article_id>\d+)$', views.get_article, name='get_article'),
    path('article/new/', views.create_post, name="create_post"),
]
