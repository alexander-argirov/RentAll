from django.contrib import messages
from django.shortcuts import redirect
from django.views import View


class CheckForRestriction:

    def dispatch(self, request, *args, **kwargs):
        if request.user.pk != kwargs['pk'] and not request.user.is_superuser:
            return redirect('index')

        data = super().dispatch(request, *args, **kwargs)
        return data


class CheckForRegisteredUser:

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and not request.user.is_superuser:
            return redirect('detail profile', pk=request.user.pk)

        data = super().dispatch(request, *args, **kwargs)
        return data


class ProfileCompletenessMixin(View):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('signin user')
        elif not request.user.profile.phone_number or not request.user.profile.first_name or not request.user.profile.last_name:
            messages.error(request, "Please fill your names and phone number"
                                    " in the profile details before creating an offer.")
            return redirect('edit profile', pk=request.user.pk)
        return super().dispatch(request, *args, **kwargs)