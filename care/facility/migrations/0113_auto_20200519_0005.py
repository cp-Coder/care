# Generated by Django 2.2.11 on 2020-05-18 18:35

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("facility", "0112_auto_20200515_1738"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="facilityuser",
            unique_together={("facility", "user")},
        ),
    ]
