# Generated by Django 3.2.4 on 2021-06-25 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jerseyshop', '0024_auto_20210625_1829'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='size',
            field=models.CharField(choices=[('Select Size', 'Select Size'), ('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL'), ('XXL', 'XXL')], default='Select Size', max_length=20),
        ),
    ]
