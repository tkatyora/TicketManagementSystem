# Generated by Django 5.0.2 on 2024-07-16 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0004_alter_admin_national_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="stsuser",
            name="code",
            field=models.CharField(max_length=6, null=True),
        ),
    ]
