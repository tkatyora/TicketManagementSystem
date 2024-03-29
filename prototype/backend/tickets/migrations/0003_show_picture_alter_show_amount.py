# Generated by Django 5.0.2 on 2024-03-06 10:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("tickets", "0002_remove_ticket_showcity_remove_ticket_showdate_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="show",
            name="picture",
            field=models.ImageField(blank=True, null=True, upload_to="pictures"),
        ),
        migrations.AlterField(
            model_name="show",
            name="amount",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
