# Generated by Django 5.1.6 on 2025-02-12 15:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("apexData", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="driver",
            name="points",
            field=models.IntegerField(default=0, verbose_name="Current Season Points"),
        ),
    ]
