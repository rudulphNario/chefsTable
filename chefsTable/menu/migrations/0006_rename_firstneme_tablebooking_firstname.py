# Generated by Django 4.2.3 on 2024-02-23 02:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0005_rename_firstname_tablebooking_firstneme'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tablebooking',
            old_name='firstNeme',
            new_name='firstName',
        ),
    ]
