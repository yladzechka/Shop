# Generated by Django 4.1.3 on 2022-12-14 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_alter_author_photo_alter_book_image_and_more'),
        ('cart', '0002_remove_cart_amount_remove_cart_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='products',
            field=models.ManyToManyField(blank=True, to='catalog.book'),
        ),
    ]
