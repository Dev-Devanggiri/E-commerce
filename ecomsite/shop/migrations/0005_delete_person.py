# Generated by Django 5.0.3 on 2024-03-20 09:13

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("shop", "0004_person"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Person",
        ),
    ]
