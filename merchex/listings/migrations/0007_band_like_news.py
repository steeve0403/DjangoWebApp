# Generated by Django 4.2.5 on 2023-09-29 07:49

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("listings", "0006_listing_delete_listings"),
    ]

    operations = [
        migrations.AddField(
            model_name="band",
            name="like_news",
            field=models.BooleanField(default=False),
        ),
    ]