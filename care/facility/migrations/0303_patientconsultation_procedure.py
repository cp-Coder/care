# Generated by Django 2.2.11 on 2022-07-25 18:06

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("facility", "0302_patientconsultation_prn_prescription"),
    ]

    operations = [
        migrations.AddField(
            model_name="patientconsultation",
            name="procedure",
            field=django.contrib.postgres.fields.jsonb.JSONField(default=dict),
        ),
    ]
