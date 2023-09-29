# Generated by Django 4.2.5 on 2023-09-29 07:45

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("listings", "0005_listings"),
    ]

    operations = [
        migrations.CreateModel(
            name="Listing",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                ("description", models.CharField(max_length=100)),
                ("sold", models.BooleanField(default=False)),
                (
                    "year",
                    models.IntegerField(
                        validators=[
                            django.core.validators.MinValueValidator(1900),
                            django.core.validators.MaxValueValidator(2021),
                        ]
                    ),
                ),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("R", "Record"),
                            ("C", "Clothing"),
                            ("P", "Poster"),
                            ("M", "Misc"),
                        ],
                        max_length=5,
                    ),
                ),
                (
                    "band",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="listings.band",
                    ),
                ),
            ],
        ),
        migrations.DeleteModel(
            name="Listings",
        ),
    ]