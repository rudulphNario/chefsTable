# Generated by Django 4.2.3 on 2024-02-23 02:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0004_rename_firstneme_tablebooking_firstname'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tablebooking',
            old_name='firstName',
            new_name='firstNeme',
        ),
    ]