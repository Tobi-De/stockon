# Generated by Django 5.1 on 2024-08-20 21:43
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("products", "0001_initial"),
        ("suppliers", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Purchase",
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
                (
                    "created",
                    model_utils.fields.AutoCreatedField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="created",
                    ),
                ),
                (
                    "modified",
                    model_utils.fields.AutoLastModifiedField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="modified",
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("PENDING", "En attente"),
                            ("RECEIVED", "Reçu"),
                            ("CANCELED", "Annulé"),
                        ],
                        default="PENDING",
                        max_length=10,
                    ),
                ),
                ("total_cost", models.PositiveIntegerField(verbose_name="Coût total")),
                (
                    "order_date",
                    models.DateField(blank=True, null=True, verbose_name="Date de commande"),
                ),
                (
                    "received_date",
                    models.DateField(blank=True, null=True, verbose_name="Date de réception"),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="purchases",
                        to="products.product",
                        verbose_name="Produit",
                    ),
                ),
                (
                    "supplier",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="purchases",
                        to="suppliers.supplier",
                        verbose_name="Fournisseur",
                    ),
                ),
            ],
            options={
                "verbose_name": "Achat",
                "verbose_name_plural": "Achats",
                "ordering": ["-created"],
            },
        ),
        migrations.CreateModel(
            name="Item",
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
                (
                    "created",
                    model_utils.fields.AutoCreatedField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="created",
                    ),
                ),
                (
                    "modified",
                    model_utils.fields.AutoLastModifiedField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="modified",
                    ),
                ),
                (
                    "quantity_ordered",
                    models.PositiveIntegerField(verbose_name="Quantité commandée"),
                ),
                (
                    "quantity_received",
                    models.PositiveIntegerField(verbose_name="Quantité reçue"),
                ),
                (
                    "unit_price",
                    models.PositiveIntegerField(verbose_name="Prix unitaire"),
                ),
                ("total_cost", models.PositiveIntegerField(verbose_name="Coût total")),
                (
                    "purchase",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="items",
                        to="purchases.purchase",
                        verbose_name="Achat",
                    ),
                ),
            ],
            options={
                "verbose_name": "Article",
                "verbose_name_plural": "Articles",
            },
        ),
    ]
