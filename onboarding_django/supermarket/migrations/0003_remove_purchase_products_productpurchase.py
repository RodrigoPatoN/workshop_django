# Generated by Django 5.1.7 on 2025-03-28 11:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("supermarket", "0002_purchase_products_delete_productpurchase"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="purchase",
            name="products",
        ),
        migrations.CreateModel(
            name="ProductPurchase",
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
                ("quantity", models.IntegerField()),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="supermarket.product",
                    ),
                ),
                (
                    "purchase",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="supermarket.purchase",
                    ),
                ),
            ],
        ),
    ]
