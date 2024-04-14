from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('RentAll.web.urls')),
    path('offers/', include('RentAll.rent_offers.urls')),
    path('accounts/', include('RentAll.accounts.urls')),
    path('articles/', include('RentAll.articles.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
