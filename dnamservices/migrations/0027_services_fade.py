# Generated by Django 4.0.3 on 2022-06-07 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dnamservices', '0026_contacts_services_detail'),
    ]

    operations = [
        migrations.AddField(
            model_name='services',
            name='fade',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
