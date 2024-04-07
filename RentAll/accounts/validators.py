from django.core.exceptions import ValidationError
import re
from django.core import exceptions



def validate_username(username):
    is_valid = all(ch.isalnum() or ch == '_' for ch in username)

    if not is_valid:
        raise ValidationError("Ensure this value contains only letters, numbers, and underscore.")

def phone_validator(value):
    match = re.match(r"^(0|\+359)(\d{9})\b", value)
    if not match:
        raise exceptions.ValidationError('Valid phone format is 0xxxxxxxxx or +359xxxxxxxxxx!')


def check_name_symbols_for_non_alphabetical(value):
    if not value.isalpha():
        raise exceptions.ValidationError('Name must be only alphabet symbol!')