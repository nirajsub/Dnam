# Generated by Django 4.0.3 on 2022-06-06 03:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dnamservices', '0016_sites_save'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sites',
            old_name='save',
            new_name='enter',
        ),
    ]
