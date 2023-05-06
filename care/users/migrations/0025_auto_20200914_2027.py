# Generated by Django 2.2.11 on 2020-09-14 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0024_auto_20200801_1844"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="user_type",
            field=models.IntegerField(
                choices=[
                    (3, "Pharmacist"),
                    (5, "Volunteer"),
                    (10, "Staff"),
                    (15, "Doctor"),
                    (25, "DistrictLabAdmin"),
                    (39, "DistrictReadOnlyAdmin"),
                    (30, "DistrictAdmin"),
                    (35, "StateLabAdmin"),
                    (40, "StateAdmin"),
                ]
            ),
        ),
    ]
