from django.contrib import admin
from django.urls import path  , include
from django.conf.urls.static import static
from . import settings
from django.views.static import serve
from django.conf.urls import url
from django.conf.urls import (
                                handler400,
                                handler403,
                                handler404,
                                handler500)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('store.urls')),
  
   url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
   url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


