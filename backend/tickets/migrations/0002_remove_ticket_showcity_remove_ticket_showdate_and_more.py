# Generated by Django 5.0.2 on 2024-07-26 13:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shows", "0003_show_created_on_alter_show_showdate_and_more"),
        ("tickets", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="ticket",
            name="showCity",
        ),
        migrations.RemoveField(
            model_name="ticket",
            name="showDate",
        ),
        migrations.RemoveField(
            model_name="ticket",
            name="showName",
        ),
        migrations.RemoveField(
            model_name="ticket",
            name="showVenue",
        ),
        migrations.AddField(
            model_name="ticket",
            name="show_detailts",
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.CASCADE, to="shows.show"
            ),
        ),
    ]
