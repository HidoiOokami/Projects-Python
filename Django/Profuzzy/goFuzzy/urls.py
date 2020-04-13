"""goFuzzy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.contrib.auth import urls

from blog import views as vws
from goFuzzy import views as goViews


urlpatterns = [
    path('jet/', include('jet.urls', 'jet')),
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),

    path('', vws.index),

    path('accidents/', goViews.accidents),
    path('calculation/', goViews.calculation),
    path('lessons/', goViews.lessons),
    path('mobility/', goViews.mobility),
    path('search/', goViews.search),
    path('system/', goViews.system),
    path('training/', goViews.training),
    path('transport/', goViews.transport),
    path('story/', goViews.story),

    path('blog/', goViews.blog),
    path('blog/post/<int:post_id>', goViews.post),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = 'Blog Profuzzy'
admin.site.index_title = 'Profuzzy '
admin.site.site_title = 'Bem Vindo'