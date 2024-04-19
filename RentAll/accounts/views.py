from django.contrib import messages
from django.contrib.auth import views as auth_views, login, logout, get_user_model
from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views import generic as views


from RentAll.accounts.forms import RentAllUserCreationForm, RentAllProfileChangePassword, ProfileForm
from RentAll.accounts.mixins import CheckForRegisteredUser, CheckForRestriction
from RentAll.accounts.models import Profile

UserModel = get_user_model()


class OwnerRequiredMixin(AccessMixin):
    """Verify that the current user has this profile."""

    def dispatch(self, request, *args, **kwargs):
        if request.user.pk != kwargs.get('pk', None):
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


class SignInUserView(auth_views.LoginView):
    template_name = 'accounts/signin_user.html'
    redirect_authenticated_user = True


class RegisterUserView(CheckForRegisteredUser, views.FormView):
    template_name = 'accounts/register_user.html'
    form_class = RentAllUserCreationForm

    def form_valid(self, form):
        email = form.cleaned_data['email']
        if UserModel.objects.filter(email=email).exists():
            messages.error(self.request, "A user with that email already exists.")
            return self.form_invalid(form)

        user = form.save()
        login(self.request, user)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('edit profile', kwargs={'pk': self.request.user.pk})


def signout_user(request):
    logout(request)
    return redirect('index')


class ProfileDetailsView(views.DetailView):
    queryset = Profile.objects \
        .prefetch_related("user") \
        .all()

    template_name = "accounts/details_profile.html"


class ProfileUpdateView(CheckForRestriction, views.UpdateView):
    queryset = Profile.objects.all()
    template_name = "accounts/edit_profile.html"
    form_class = ProfileForm

    def get_success_url(self):
        return reverse("detail profile", kwargs={"pk": self.object.pk})


class PasswordChange(auth_views.PasswordChangeView):
    template_name = 'accounts/password_change.html'
    model = UserModel
    form_class = RentAllProfileChangePassword

    def get_success_url(self):
        return reverse_lazy('detail profile', kwargs={'pk': self.request.user.pk})


class ProfileDeleteView(views.DeleteView):
    template_name = 'accounts/delete_profile.html'
    model = UserModel
    success_url = reverse_lazy('index')