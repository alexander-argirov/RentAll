from django.urls import path, include

from RentAll.web.views import IndexView

urlpatterns = (
    path('', IndexView.as_view(), name='index'),
    path("accounts/", include("RentAll.accounts.urls")),
)