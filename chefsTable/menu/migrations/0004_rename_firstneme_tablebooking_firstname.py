# Generated by Django 4.2.3 on 2024-02-23 02:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_alter_tablebooking_phonenumber'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tablebooking',
            old_name='firstNeme',
            new_name='firstName',
        ),
    ]