# bookstore_project/urls.py
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # User management
    path('accounts/', include('allauth.urls')),

    # Django admin
    path('admin/', admin.site.urls),

    # Local apps
    path('', include('pages.urls')),
    path('accounts/', include('users.urls')),
    path('books/', include('books.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('_debug_/', include(debug_toolbar.urls)),
    ] + urlpatterns
