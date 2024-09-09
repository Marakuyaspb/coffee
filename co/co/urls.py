from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include
from django.contrib import admin

from main import views
from main import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
]


urlpatterns += static(
    settings.STATIC_URL, 
    document_root=settings.STATIC_ROOT
)
urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)