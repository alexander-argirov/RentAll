from django.apps import AppConfig


class AccountConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'RentAll.accounts'

    def ready(self):
        import RentAll.accounts.signals