# Generated by Django 4.1 on 2022-09-08 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Product",
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
                ("desc", models.TextField(max_length=100)),
                ("image", models.ImageField(upload_to="")),
                ("price", models.CharField(max_length=100)),
                ("unique_id", models.CharField(max_length=100)),
            ],
        ),
    ]
