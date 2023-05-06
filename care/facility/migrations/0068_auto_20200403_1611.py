# Generated by Django 2.2.11 on 2020-04-03 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("facility", "0067_auto_20200402_1841"),
    ]

    operations = [
        migrations.AddField(
            model_name="historicalpatientregistration",
            name="ongoing_medication",
            field=models.TextField(
                blank=True,
                default="",
                verbose_name="Already pescribed medication if any",
            ),
        ),
        migrations.AddField(
            model_name="patientregistration",
            name="ongoing_medication",
            field=models.TextField(
                blank=True,
                default="",
                verbose_name="Already pescribed medication if any",
            ),
        ),
    ]
