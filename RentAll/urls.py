from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve
from RentAll.web import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('RentAll.web.urls')),
    path('offers/', include('RentAll.rent_offers.urls')),
    path('accounts/', include('RentAll.accounts.urls')),
    path('articles/', include('RentAll.articles.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
handler404 = views.handle_404

if not settings.DEBUG:
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT, }),
    ]
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)