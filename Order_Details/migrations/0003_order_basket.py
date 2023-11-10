# Generated by Django 4.2.3 on 2023-08-12 23:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Cart_Details', '0008_remove_cart_order'),
        ('Order_Details', '0002_remove_order_basket'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='basket',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Cart_Details.cart'),
            preserve_default=False,
        ),
    ]