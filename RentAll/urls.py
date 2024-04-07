
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('RentAll.web.urls')),
    path('accounts/', include('RentAll.accounts.urls')),

]
