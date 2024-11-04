# Generated by Django 5.1 on 2024-11-02 21:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
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
                ("slug", models.SlugField(blank=True)),
                ("name", models.CharField(max_length=50)),
                ("name_en", models.CharField(max_length=50, null=True)),
                ("name_fr", models.CharField(max_length=50, null=True)),
                ("description", models.TextField(max_length=1000)),
                ("description_en", models.TextField(max_length=1000, null=True)),
                ("description_fr", models.TextField(max_length=1000, null=True)),
                ("position", models.SmallIntegerField()),
                ("icon", models.FileField(max_length=150, upload_to="")),
            ],
        ),
        migrations.CreateModel(
            name="PaymentMethod",
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
                ("name", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="TypeDeal",
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
                ("name", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Deal",
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
                ("contact", models.CharField(max_length=100)),
                (
                    "status",
                    models.SlugField(
                        choices=[
                            ("Running", "Running"),
                            ("Waiting", "Waiting"),
                            ("Cancelled", "Cancelled"),
                        ]
                    ),
                ),
                ("program", models.URLField()),
                ("start_date", models.DateField(null=True)),
                ("end_date", models.DateField(null=True)),
                (
                    "amount_paid",
                    models.DecimalField(decimal_places=2, max_digits=10, null=True),
                ),
                (
                    "amount_available",
                    models.DecimalField(decimal_places=2, max_digits=10, null=True),
                ),
                ("potential", models.SmallIntegerField(default=0)),
                ("comment", models.TextField(max_length=500, null=True)),
                (
                    "payment_method",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="websites.paymentmethod",
                    ),
                ),
                ("type", models.ManyToManyField(to="websites.typedeal")),
            ],
        ),
        migrations.CreateModel(
            name="Website",
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
                ("slug", models.SlugField(blank=True, max_length=100)),
                ("name", models.CharField(max_length=100)),
                ("url", models.URLField(max_length=250)),
                ("icon", models.FileField(max_length=150, upload_to="")),
                ("screen", models.FileField(max_length=150, upload_to="")),
                ("is_direct_link", models.BooleanField()),
                ("description", models.TextField(max_length=10000)),
                ("description_en", models.TextField(max_length=10000, null=True)),
                ("description_fr", models.TextField(max_length=10000, null=True)),
                ("update_date", models.DateField()),
                ("end_date", models.DateField(blank=True, null=True)),
                ("click", models.PositiveBigIntegerField(default=0)),
                (
                    "category",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="websites.category",
                    ),
                ),
                (
                    "deal",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="websites.deal",
                    ),
                ),
            ],
        ),
        migrations.AddIndex(
            model_name="deal",
            index=models.Index(fields=["status"], name="websites_de_status_56b27b_idx"),
        ),
    ]