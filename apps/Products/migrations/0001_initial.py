# Generated by Django 4.2.7 on 2023-12-05 14:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Kategori",
            fields=[
                ("id_kategori", models.BigAutoField(primary_key=True, serialize=False)),
                (
                    "nama_kategori",
                    models.CharField(max_length=250, null=True, unique=True),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Status",
            fields=[
                ("id_status", models.BigAutoField(primary_key=True, serialize=False)),
                ("nama_status", models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name="Produk",
            fields=[
                ("id_produk", models.BigAutoField(primary_key=True, serialize=False)),
                ("nama_produk", models.CharField(max_length=250)),
                ("harga", models.DecimalField(decimal_places=4, max_digits=19)),
                (
                    "kategori",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="Products.kategori",
                    ),
                ),
                (
                    "status",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="Products.status",
                    ),
                ),
            ],
        ),
    ]
