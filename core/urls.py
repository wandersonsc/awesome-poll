from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include

from django.views.generic.base import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),

    # home
    path('', TemplateView.as_view(template_name='home.html'), name='home'),

    # polls
    path('polls/', include('polls.urls', namespace='polls')),

    # accounts
    path('account/', include('accounts.urls', namespace='accounts')),
    path('account/', include('django.contrib.auth.urls')),

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    # urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
