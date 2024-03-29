# Generated by Django 5.0.2 on 2024-03-06 20:47

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("tickets", "0008_alter_show_numbertickets"),
    ]

    operations = [
        migrations.AddField(
            model_name="ticket",
            name="showStatus",
            field=models.CharField(
                choices=[
                    ("inside", "Inside The show"),
                    ("outSide", "Outside The show"),
                ],
                default="Out Side Show",
                max_length=100,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="ticket",
            name="ticketStatus",
            field=models.CharField(
                choices=[
                    ("valid", "valid"),
                    ("expired", "expired"),
                    ("deleted", "deleted"),
                    ("updated", "updated"),
                ],
                default="Valid",
                max_length=100,
                null=True,
            ),
        ),
    ]
