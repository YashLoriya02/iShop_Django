# Generated by Django 4.1.3 on 2023-04-29 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_product_category_product_image_product_price_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(default='', max_length=50)),
                ('phone', models.IntegerField(default=0)),
                ('desc', models.CharField(max_length=500)),
            ],
        ),
    ]
