# Generated by Django 5.0.2 on 2024-07-16 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0005_stsuser_code"),
    ]

    operations = [
        migrations.AddField(
            model_name="stsuser",
            name="token",
            field=models.TextField(null=True),
        ),
    ]