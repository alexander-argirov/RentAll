from django import forms
from django.contrib.auth import forms as auth_forms, get_user_model, password_validation

from RentAll.accounts.models import Profile

UserModel = get_user_model()


class RentAllUserCreationForm(auth_forms.UserCreationForm):
    user = None

    class Meta(auth_forms.UserCreationForm.Meta):
        model = UserModel
        fields = ('email',)


class RentAllChangeForm(auth_forms.UserChangeForm):
    class Meta(auth_forms.UserChangeForm.Meta):
        model = UserModel


class RentAllProfileChangePassword(auth_forms.PasswordChangeForm):
    old_password = forms.CharField(
        label='',
        widget=forms.PasswordInput(
            attrs={
                "autocomplete": "current-password",
                'placeholder': 'Enter your old password',
                'style': "height: 55px",
            }
        ),
    )
    new_password1 = forms.CharField(
        label='',
        widget=forms.PasswordInput(attrs={
            "autocomplete": "new-password",
            'placeholder': 'Enter your new password',
            'style': "height: 55px",
        }
        ),
        help_text=password_validation.password_validators_help_text_html(),
    )
    new_password2 = forms.CharField(
        label='',
        widget=forms.PasswordInput(
            attrs={
                "autocomplete": "new-password",
                'placeholder': 'New password confirmation',
                'style': "height: 55px",
            }
        ),
    )


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["first_name", "last_name", "phone_number", "profile_picture"]
        widgets = {
            "first_name": forms.TextInput(attrs={"placeholder": "Enter your first name"}),
            "last_name": forms.TextInput(attrs={"placeholder": "Enter your last name"}),
            "phone_number": forms.TextInput(attrs={"placeholder": "Enter your phone numb."}),
        }