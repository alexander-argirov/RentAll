# Generated by Django 5.0.3 on 2024-04-12 09:48

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rent_offers', '0005_alter_camperscaravans_type'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='camperscaravans',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='campers_caravans_owner', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='car',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='car_owner', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='van',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='van_owner', to=settings.AUTH_USER_MODEL),
        ),
    ]
