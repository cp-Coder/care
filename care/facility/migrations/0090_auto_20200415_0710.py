# Generated by Django 2.2.11 on 2020-04-15 01:40

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("facility", "0089_auto_20200413_2036"),
    ]

    operations = [
        migrations.AlterField(
            model_name="facility",
            name="facility_type",
            field=models.IntegerField(
                choices=[
                    (1, "Educational Inst"),
                    (2, "Private Hospital"),
                    (3, "Other"),
                    (4, "Hostel"),
                    (5, "Hotel"),
                    (6, "Lodge"),
                    (7, "TeleMedicine"),
                    (8, "Govt Hospital"),
                    (200, "Primary Health Centres"),
                    (201, "24x7 Public Health Centres"),
                    (202, "Family Health Centres"),
                    (203, "Community Health Centres"),
                    (220, "Urban Primary Health Center"),
                    (230, "Taluk Hospitals"),
                    (231, "Taluk Headquarters Hospitals"),
                    (240, "Women and Child Health Centres"),
                    (250, "General hospitals"),
                    (260, "District Hospitals"),
                    (850, "Testing Labs"),
                ]
            ),
        ),
    ]
