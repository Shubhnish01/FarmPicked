# Generated by Django 4.2 on 2023-05-05 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        
    ]

    operations = [
        migrations.CreateModel(
            name='Customer_Service_Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CSR_name', models.CharField(max_length=50)),
                ('CSR_email', models.CharField(max_length=60)),
                ('CSR_phone', models.CharField(max_length=12)),
                ('CSR_Subject', models.CharField(max_length=100)),
                ('CSR_message', models.TextField()),
            ],
        ),
        
    ]
