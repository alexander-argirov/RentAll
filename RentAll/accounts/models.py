from django.conf import settings
from django.core.validators import MinLengthValidator
from django.db import models
from django.contrib.auth.models import Group, Permission, User

from django.utils.translation import gettext_lazy as _
from django.contrib.auth import models as auth_models

from django.utils import timezone

from RentAll.accounts.manager import RentAllUserManager
from RentAll.accounts.validators import phone_validator, check_name_symbols_for_non_alphabetical


class RentAllUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):

    email = models.EmailField(
        _("email address"),
        unique=True,
    )

    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)

    is_staff = models.BooleanField(
        default=False,
    )

    is_active = models.BooleanField(
        default=True,
    )

    USERNAME_FIELD = "email"

    objects = RentAllUserManager()

    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        related_name='rentall_user_groups',
        related_query_name='rentall_user',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        related_name='rentall_user_permissions',
        related_query_name='rentall_user',
    )


class Profile(models.Model):
    MAX_USERNAME_LENGTH = 15
    MIN_USERNAME_LENGTH = 2
    MAX_FIRST_NAME_LENGTH = 15
    MIN_FIRST_NAME_LENGTH = 2
    MAX_LAST_NAME_LENGTH = 15
    MIN_LAST_NAME_LENGTH = 2
    MAX_PHONE_NUMBER_LENGTH = 15

    first_name = models.CharField(
        max_length=MAX_FIRST_NAME_LENGTH,
        validators=(
            MinLengthValidator(MIN_FIRST_NAME_LENGTH),
            check_name_symbols_for_non_alphabetical,
        ),
        blank=True,
        null=True,
    )

    last_name = models.CharField(
        max_length=MAX_LAST_NAME_LENGTH,
        validators=(
            MinLengthValidator(MIN_LAST_NAME_LENGTH),
            check_name_symbols_for_non_alphabetical,
        ),
        blank=True,
        null=True,
    )

    profile_picture = models.ImageField(
        upload_to='profile_pictures/',
        blank=True,
        null=True,
    )

    date_of_birth = models.DateField(
        blank=True,
        null=True
    )

    phone_number = models.CharField(
        validators=(
            phone_validator,),
        max_length=MAX_PHONE_NUMBER_LENGTH,
        blank=True,
        null=True,
    )

    user = models.OneToOneField(
        RentAllUser,
        primary_key=True,
        on_delete=models.CASCADE,
    )

    @property
    def full_name(self):
        if self.first_name and self.last_name:
            return f'{self.first_name} {self.last_name}'

        return self.first_name or self.last_name



