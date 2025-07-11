# Generated by Django 5.2.3 on 2025-06-14 22:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("productos", "0005_tipopedido"),
    ]

    operations = [
        migrations.CreateModel(
            name="Producto",
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
                ("nombre", models.CharField(max_length=100, unique=True)),
                ("cantidad", models.PositiveIntegerField()),
                ("fecha_produccion", models.DateField()),
                (
                    "material",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="productos.material",
                    ),
                ),
                (
                    "vestimenta",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="productos.cliente",
                    ),
                ),
            ],
            options={
                "verbose_name": "Producto",
                "verbose_name_plural": "Productos",
                "db_table": "producto",
            },
        ),
        migrations.CreateModel(
            name="Pedido",
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
                ("nombre", models.CharField(max_length=100, unique=True)),
                ("cantidad", models.PositiveIntegerField()),
                ("fecha_pedido", models.DateField()),
                (
                    "cliente",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="productos.cliente",
                    ),
                ),
                (
                    "tipo_pedido",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="productos.tipopedido",
                    ),
                ),
                (
                    "producto",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="productos.producto",
                    ),
                ),
            ],
            options={
                "verbose_name": "Pedido",
                "verbose_name_plural": "Pedidos",
                "db_table": "pedidos",
            },
        ),
        migrations.CreateModel(
            name="Venta",
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
                ("descripcion", models.TextField()),
                ("precio", models.DecimalField(decimal_places=0, max_digits=10)),
                ("fecha_venta", models.DateField()),
                (
                    "pedido",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="productos.pedido",
                    ),
                ),
                (
                    "tipo_pago",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="productos.tipopago",
                    ),
                ),
            ],
            options={
                "verbose_name": "Venta",
                "verbose_name_plural": "Ventas",
                "db_table": "venta",
            },
        ),
    ]
