# Generated by Django 4.2.5 on 2023-09-28 14:35

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("listings", "0003_band_high"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="band",
            name="high",
        ),
    ]
