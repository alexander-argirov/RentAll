# Generated by Django 5.0.3 on 2024-04-10 08:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rent_offers', '0003_alter_camperscaravans_owner_alter_car_owner_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='camperscaravans',
            old_name='vehicle_type',
            new_name='type',
        ),
    ]
