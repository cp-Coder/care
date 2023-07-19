# Generated by Django 4.2.2 on 2023-07-19 11:47

import django.db.models.deletion
from django.db import migrations, models


def forwards_func(apps, schema_editor):
    patient_notes_model = apps.get_model("facility", "PatientNotes")
    patient_notes = patient_notes_model.objects.all()
    for patient_note in patient_notes:
        if patient_note.patient.last_consultation:
            patient_note.consultation = patient_note.patient.last_consultation
            patient_note.save()


class Migration(migrations.Migration):
    dependencies = [
        ("facility", "0372_assetavailabilityrecord"),
    ]

    operations = [
        migrations.AddField(
            model_name="patientnotes",
            name="consultation",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="facility.patientconsultation",
            ),
        ),
        migrations.RunPython(forwards_func),
    ]