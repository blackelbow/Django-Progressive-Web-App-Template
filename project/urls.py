from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
    url('', include('pwa.urls')),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^accounts/', include('allauth.urls')),
    path('api/', include('api.urls')),
    path('mobile/', include('mobile.urls')),

]
