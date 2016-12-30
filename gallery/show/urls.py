"""gallery URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.conf.urls.static import static
from . import views
from django.conf import settings
from . import api

urlpatterns = [
    url(r'^$', views.show_index, name='show_index'),
    url(r'^random/', views.show_random_images, name='show_random_images'),
    url(r'^search/(?P<search>[,\w-]+/$)', views.search, name="search"),
    url(r'^delete/(?P<delete>[0-9]+/$)', views.delete, name="delete"),
    url(r'^unsplash/', views.unsplash, name="unsplash"),
    url(r'^logout/', views.logoutu, name="logout"),
    url(r'^upload/', views.UploadView.as_view(), name="upload"),
    url(r'^login/', views.UserCheck.as_view(), name='login'),
    url(r'^register/', views.UserFormView.as_view(), name='register'),
    #api stuff
    url(r'^api/images/(?P<pk>[0-9]+)/$', api.PhotoDetail.as_view()),
    url(r'^api/images/', api.PhotoList.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
