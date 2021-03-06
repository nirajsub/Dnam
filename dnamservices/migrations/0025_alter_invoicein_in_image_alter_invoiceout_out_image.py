# Generated by Django 4.0.3 on 2022-06-06 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dnamservices', '0024_alter_invoicein_in_image_alter_invoiceout_out_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoicein',
            name='in_image',
            field=models.FileField(blank=True, null=True, upload_to='Invoice_in'),
        ),
        migrations.AlterField(
            model_name='invoiceout',
            name='out_image',
            field=models.FileField(blank=True, null=True, upload_to='Invoice_out'),
        ),
    ]
