from django.urls import path, include

from RentAll.rent_offers.views import CarCreateOfferView, CommonOffersView, CarDetailView, CarDeleteView, \
    CarUpdateView, CarListView, VanListView, VanCreateOfferView, VanDetailView, CamperCaravanListView, \
    CamperCaravanCreateOfferView, CamperCaravanDetailView, CamperCaravanUpdateView, CamperCaravanDeleteView, \
    VanUpdateView, VanDeleteView

urlpatterns = [
    path('', CommonOffersView.as_view(), name='common offers view'),
    path('cars/', include([
        path('', CarListView.as_view(), name='cars list'),
        path('create/', CarCreateOfferView.as_view(), name='create car'),
        path('detail/<int:pk>/', CarDetailView.as_view(), name='car detail'),
        path('edit/<int:pk>/', CarUpdateView.as_view(), name='edit car'),
        path('delete/<int:pk>/', CarDeleteView.as_view(), name='delete car'),
    ])),
    path('vans/', include([
        path('', VanListView.as_view(), name='vans list'),
        path('create/', VanCreateOfferView.as_view(), name='create van'),
        path('detail/<int:pk>/', VanDetailView.as_view(), name='van detail'),
        path('edit/<int:pk>/', VanUpdateView.as_view(), name='edit van'),
        path('delete/<int:pk>/', VanDeleteView.as_view(), name='delete van'),
    ])),
    path('campers_caravans/', include([
        path('', CamperCaravanListView.as_view(), name='campers and caravans list'),
        path('create/', CamperCaravanCreateOfferView.as_view(), name='create cam_car'),
        path('detail/<int:pk>/', CamperCaravanDetailView.as_view(), name='cam_car detail'),
        path('edit/<int:pk>/', CamperCaravanUpdateView.as_view(), name='edit cam_car'),
        path('delete/<int:pk>/', CamperCaravanDeleteView.as_view(), name='delete cam_car'),
    ])),
]
