# Generated by Django 3.2.4 on 2021-06-26 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jerseyshop', '0026_order_complete'),
    ]

    operations = [
        migrations.AddField(
            model_name='shippinginfo',
            name='email',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='shippinginfo',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]