# Generated by Django 4.2 on 2023-05-25 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_homepageproductfruits_product_category_product_image_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomepageProductVegetable',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('image', models.ImageField(default='', upload_to='shop/images')),
                ('product_name', models.CharField(max_length=50)),
                ('category', models.CharField(default='', max_length=50)),
                ('price', models.IntegerField(default=0)),
                ('pub_date', models.DateField()),
            ],
        ),
    ]
