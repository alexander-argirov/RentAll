
from RentAll.accounts.models import RentAllUser


from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from RentAll.accounts.models import RentAllUser


class Vehicle(models.Model):
    MAX_BRAND_LENGTH = 15
    MIN_BRAND_LENGTH = 2
    MAX_MODEL_LENGTH = 20
    MIN_MODEL_LENGTH = 2
    MAX_GEARS_LENGTH = 10
    MIN_PRICE = 1.00

    GEAR_CHOICES = (
        ('manual', 'Manual'),
        ('automatic', 'Automatic'),
    )

    ENGINE_CHOICES = (
        ('diesel', 'Diesel'),
        ('petrol', 'Petrol'),
        ('electric', 'Electric'),
        ('LPG', 'LPG'),
    )

    brand = models.CharField(
        max_length=MAX_BRAND_LENGTH,
        validators=[MinLengthValidator(MIN_BRAND_LENGTH)],
        blank=False,
        null=False,
    )

    model = models.CharField(
        max_length=MAX_MODEL_LENGTH,
        validators=[MinLengthValidator(MIN_MODEL_LENGTH)],
        blank=False,
        null=False,
    )

    first_registration = models.PositiveIntegerField()

    type_of_engine = models.CharField(
        max_length=10,
        choices=ENGINE_CHOICES,
        blank=False,
        null=False,
    )

    type_of_gear = models.CharField(
        max_length=MAX_GEARS_LENGTH,
        choices=GEAR_CHOICES,
        blank=False,
        null=False,
    )

    seats = models.PositiveSmallIntegerField(
        blank=False,
        null=False,
    )

    vehicle_image = models.ImageField(
        blank=False,
        null=False,
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(MIN_PRICE)],
        blank=False,
        null=False,
    )

    owner = models.ForeignKey(
        RentAllUser,
        on_delete=models.CASCADE,

    )

    class Meta:
        abstract = True


class Car(Vehicle):
    CAR_TYPE_LENGTH = 10
    CAR_TYPE_CHOICES = (
        ('sedan', 'Sedan'),
        ('SUV', 'SUV'),
        ('coupe', 'Coupe'),
        ('cabriolet', 'Cabriolet'),
        ('estate car', 'Estate Car'),
    )

    car_type = models.CharField(
        max_length=CAR_TYPE_LENGTH,
        choices=CAR_TYPE_CHOICES,
        blank=False,
        null=False,
    )


class Van(Vehicle):
    payload_weight = models.PositiveIntegerField(
        blank=False,
        null=False,
    )


class CampersCaravans(Vehicle):
    MAX_BRAND_LENGTH = 15
    MIN_BRAND_LENGTH = 2
    MAX_TYPE_LENGTH = 10
    TYPE_CHOICES = (
        ('caravan', 'Caravan'),
        ('camper', 'Camper'),
    )

    vehicle_type = models.CharField(
        max_length=MAX_TYPE_LENGTH,
        choices=TYPE_CHOICES,
        blank=False,
        null=False,
    )


