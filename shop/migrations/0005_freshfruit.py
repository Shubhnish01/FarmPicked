# Generated by Django 4.2 on 2023-05-25 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_rename_product_id_homepageproductvegetable_vege_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='FreshFruit',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('image', models.ImageField(default='', upload_to='shop/images')),
                ('product_name', models.CharField(max_length=50)),
                ('per_off', models.CharField(max_length=50)),
                ('category', models.CharField(default='', max_length=50)),
                ('price', models.CharField(max_length=30)),
                ('pub_date', models.DateField()),
            ],
        ),
    ]