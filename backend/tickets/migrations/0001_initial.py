# Generated by Django 5.0.2 on 2024-07-10 07:56

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Ticket",
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
                ("showName", models.CharField(max_length=255, null=True)),
                ("customerName", models.CharField(max_length=255, null=True)),
                ("showVenue", models.CharField(blank=True, max_length=255, null=True)),
                (
                    "showCity",
                    models.CharField(
                        choices=[
                            ("Harare", "Harare"),
                            ("Bulawayo", "Bulawayo"),
                            ("Gweru", "Gweru"),
                            ("Chitungwiza", "Chitungwiza"),
                            ("Mutare", "Mutare"),
                            ("Kwekwe", "Kwekwe"),
                            ("Kadoma", "Kadoma"),
                            ("Masvingo", "Masvingo"),
                            ("Norton", "Norton"),
                            ("Chinhoyi", "Chinhoyi"),
                        ],
                        default="Not Selected",
                        max_length=100,
                        null=True,
                    ),
                ),
                ("showDate", models.DateTimeField(null=True)),
                ("created_on", models.DateTimeField(auto_now_add=True, null=True)),
                ("updated_on", models.DateTimeField(auto_now=True, null=True)),
                (
                    "qr_code",
                    models.ImageField(blank=True, null=True, upload_to="Pictures"),
                ),
                ("amountPaid", models.IntegerField(null=True)),
                ("numberPeople", models.IntegerField(null=True)),
                (
                    "created_by",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
