# Generated by Django 3.2.4 on 2021-06-20 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jerseyshop', '0002_rename_jerseydetails_clubjerseydetails'),
    ]

    operations = [
        migrations.CreateModel(
            name='NTJerseyDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('price', models.CharField(max_length=50)),
                ('image', models.ImageField(blank=True, null=True, upload_to='img/')),
                ('availabilty', models.CharField(choices=[('In Stock', 'In Stock'), ('Out of Stock', 'Out of Stock')], max_length=50)),
                ('description', models.CharField(max_length=500)),
            ],
        ),
    ]
