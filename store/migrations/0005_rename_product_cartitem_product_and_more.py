# Generated by Django 4.1.4 on 2022-12-29 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_orderitem_zip'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartitem',
            old_name='Product',
            new_name='product',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='Collection',
            new_name='collection',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='zip',
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='unit_price',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
    ]
