# Generated by Django 4.2 on 2023-05-05 08:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Feedback', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedback',
            old_name='comment',
            new_name='fb_comment',
        ),
        migrations.RenameField(
            model_name='feedback',
            old_name='name',
            new_name='fb_name',
        ),
        migrations.RenameField(
            model_name='feedback',
            old_name='phone',
            new_name='fb_phone',
        ),
    ]
