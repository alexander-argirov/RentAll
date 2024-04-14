from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views import generic as views

from .models import Car, Van, CampersCaravans
from .forms import CarForm, VanForm, CampersCaravansForm
from ..accounts.models import Profile


class CommonOffersView(views.TemplateView):
    template_name = 'rent_offers/offers_common.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['offers'] = []
        for queryset_offers in (
                Car.objects.all().order_by('-published')[:5],
                Van.objects.all().order_by('-published')[:5],
                CampersCaravans.objects.all().order_by('-published')[:5]
        ):
            context['offers'].extend(queryset_offers)

        return context


class CarListView(views.ListView):
    template_name = 'rent_offers/cars/list_cars.html'
    model = Car
    paginate_by = 3

    def get_queryset(self):
        queryset = super().get_queryset().order_by('published')

        for field, value in self.request.GET.items():
            if value and field != 'page':
                queryset = queryset.filter(**{field: value})

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paginator = Paginator(context['object_list'], self.paginate_by)
        page = self.request.GET.get('page')

        try:
            cars = paginator.page(page)
        except PageNotAnInteger:
            cars = paginator.page(1)
        except EmptyPage:
            cars = paginator.page(paginator.num_pages)

        context['cars'] = cars
        return context


class CarCreateOfferView(views.CreateView):
    model = Car
    form_class = CarForm
    template_name = 'rent_offers/cars/create_car.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        profile = get_object_or_404(Profile, user=self.request.user)
        owner = profile.user
        form.instance.owner = owner
        return super().form_valid(form)


class CarDetailView(views.DetailView):
    model = Car
    template_name = 'rent_offers/cars/car_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Car'] = get_object_or_404(Car, pk=self.kwargs['pk'])
        context['Car_image'] = Car.vehicle_image
        return context


class CarUpdateView(LoginRequiredMixin, UserPassesTestMixin, views.UpdateView):
    model = Car
    fields = ['brand', 'model', 'first_registration', 'type_of_engine', 'type_of_gear', 'seats', 'vehicle_image',
              'price', 'city']
    template_name = 'rent_offers/cars/update_car.html'
    success_url = reverse_lazy('common offers view')

    def test_func(self):
        car = self.get_object()
        user = self.request.user
        return user == car.owner or user.is_superuser


class CarDeleteView(views.DeleteView):
    model = Car
    template_name = 'rent_offers/cars/car_confirm_delete.html'
    success_url = reverse_lazy('common offers view')


class VanListView(views.ListView):
    template_name = 'rent_offers/vans/list_vans.html'
    model = Van
    paginate_by = 3

    def get_queryset(self):
        queryset = super().get_queryset().order_by('published')

        for field, value in self.request.GET.items():
            if value and field != 'page':
                queryset = queryset.filter(**{field: value})

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paginator = Paginator(context['object_list'], self.paginate_by)
        page = self.request.GET.get('page')

        try:
            vans = paginator.page(page)
        except PageNotAnInteger:
            vans = paginator.page(1)
        except EmptyPage:
            vans = paginator.page(paginator.num_pages)

        context['vans'] = vans
        return context


class VanCreateOfferView(views.CreateView):
    model = Van
    form_class = VanForm
    template_name = 'rent_offers/vans/create_van.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        profile = get_object_or_404(Profile, user=self.request.user)
        owner = profile.user
        form.instance.owner = owner
        return super().form_valid(form)


class VanDetailView(views.DetailView):
    model = Van
    template_name = 'rent_offers/vans/van_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Van'] = get_object_or_404(Van, pk=self.kwargs['pk'])
        context['Van_image'] = Van.vehicle_image
        return context


class VanUpdateView(LoginRequiredMixin, UserPassesTestMixin, views.UpdateView):
    model = Van
    fields = ['brand', 'model', 'first_registration', 'type_of_engine', 'type_of_gear',
              'payload_weight', 'seats', 'vehicle_image', 'city',]
    template_name = 'rent_offers/vans/update_van.html'
    success_url = reverse_lazy('common offers view')

    def test_func(self):
        van = self.get_object()
        user = self.request.user
        return user == van.owner or user.is_superuser


class VanDeleteView(views.DeleteView):
    model = Van
    template_name = 'rent_offers/vans/van_confirm_delete.html'
    success_url = reverse_lazy('common offers view')


class CamperCaravanListView(views.ListView):
    template_name = 'rent_offers/campers_caravans/list_campers_caravans.html'
    model = CampersCaravans
    paginate_by = 3

    def get_queryset(self):
        queryset = super().get_queryset().order_by('published')

        for field, value in self.request.GET.items():
            if value and field != 'page':
                queryset = queryset.filter(**{field: value})

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paginator = Paginator(context['object_list'], self.paginate_by)
        page = self.request.GET.get('page')

        try:
            campers_caravans = paginator.page(page)
        except PageNotAnInteger:
            campers_caravans = paginator.page(1)
        except EmptyPage:
            campers_caravans = paginator.page(paginator.num_pages)

        context['campers_caravans'] = campers_caravans
        return context


class CamperCaravanCreateOfferView(views.CreateView):
    model = CampersCaravans
    form_class = CampersCaravansForm
    template_name = 'rent_offers/campers_caravans/create_campers_caravans.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        profile = get_object_or_404(Profile, user=self.request.user)
        owner = profile.user
        form.instance.owner = owner
        return super().form_valid(form)


class CamperCaravanDetailView(views.DetailView):
    model = CampersCaravans
    template_name = 'rent_offers/campers_caravans/camper_caravan_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['campers_caravans'] = get_object_or_404(CampersCaravans, pk=self.kwargs['pk'])
        context['campers_caravans_image'] = CampersCaravans.vehicle_image
        return context


class CamperCaravanUpdateView(LoginRequiredMixin, UserPassesTestMixin, views.UpdateView):
    model = CampersCaravans
    fields = ['brand', 'model', 'first_registration', 'type_of_engine', 'type_of_gear', 'seats', 'vehicle_image',
              'price', 'city', 'type']
    template_name = 'rent_offers/campers_caravans/update_campers_caravans.html'
    success_url = reverse_lazy('common offers view')

    def test_func(self):
        camper_caravan = self.get_object()
        user = self.request.user
        return user == camper_caravan.owner or user.is_superuser


class CamperCaravanDeleteView(views.DeleteView):
    model = CampersCaravans
    template_name = 'rent_offers/campers_caravans/camper_caravan_confirm_delete.html'
    success_url = reverse_lazy('common offers view')
