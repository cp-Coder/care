# Generated by Django 2.2.11 on 2020-09-21 11:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0029_ward"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="ward",
            unique_together={("local_body", "name", "number")},
        ),
    ]
