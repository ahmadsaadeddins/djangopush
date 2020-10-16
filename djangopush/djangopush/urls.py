from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from .views import home, send_push

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('send_push', send_push),
    path('webpush/', include('webpush.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
