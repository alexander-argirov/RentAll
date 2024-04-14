from django.urls import path, include

from RentAll.web.views import IndexView, ContactsView

urlpatterns = (
    path('', IndexView.as_view(), name='index'),
    path('contactus/', ContactsView.as_view(), name='contacts'),
)