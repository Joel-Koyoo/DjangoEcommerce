# Generated by Django 4.1.4 on 2023-01-11 20:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_alter_customer_options_remove_customer_email_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'permissions': [('cancel_order', 'Can Cancel Order')]},
        ),
    ]