# Generated by Django 4.0.3 on 2022-06-06 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dnamservices', '0020_invoicein_delete_invoiceout_delete'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoicein',
            name='name',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='invoiceout',
            name='name',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
