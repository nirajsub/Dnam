# Generated by Django 4.0.3 on 2022-06-05 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dnamservices', '0008_workordertask_show'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='delete',
            field=models.BooleanField(default=False),
        ),
    ]
