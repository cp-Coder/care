# Generated by Django 2.2.11 on 2020-03-28 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("facility", "0038_merge_20200328_1433"),
    ]

    operations = [
        migrations.AlterField(
            model_name="facility",
            name="facility_type",
            field=models.IntegerField(
                choices=[
                    (1, "Educational Inst"),
                    (2, "Hospital"),
                    (3, "Other"),
                    (4, "Hostel"),
                    (5, "Hotel"),
                    (6, "Lodge"),
                ]
            ),
        ),
    ]
