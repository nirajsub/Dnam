# Generated by Django 4.0.3 on 2022-06-06 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dnamservices', '0015_remove_sites_save'),
    ]

    operations = [
        migrations.AddField(
            model_name='sites',
            name='save',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]