from django.conf.urls import include,url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('show.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
