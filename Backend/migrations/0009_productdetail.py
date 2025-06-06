# Generated by Django 4.1.5 on 2023-02-01 13:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("amazon_backend_api", "0008_product"),
    ]

    operations = [
        migrations.CreateModel(
            name="ProductDetail",
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
                ("created_at", models.DateTimeField(auto_now_add=True, null=True)),
                ("updated_at", models.DateTimeField(auto_now=True, null=True)),
                (
                    "description",
                    models.TextField(
                        max_length=1000, verbose_name="Product Descriptions"
                    ),
                ),
                (
                    "mrp",
                    models.DecimalField(
                        decimal_places=2, max_digits=10, verbose_name="MRP"
                    ),
                ),
                (
                    "discount",
                    models.DecimalField(
                        decimal_places=2, max_digits=10, verbose_name="Discount"
                    ),
                ),
                (
                    "image1",
                    models.ImageField(upload_to="products", verbose_name="Image 1"),
                ),
                (
                    "image2",
                    models.ImageField(upload_to="products", verbose_name="Image 2"),
                ),
                (
                    "image3",
                    models.ImageField(upload_to="products", verbose_name="Image 3"),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="product",
                        to="amazon_backend_api.product",
                    ),
                ),
                (
                    "size",
                    models.ManyToManyField(
                        related_name="size", to="amazon_backend_api.size"
                    ),
                ),
            ],
            options={"abstract": False,},
        ),
    ]
