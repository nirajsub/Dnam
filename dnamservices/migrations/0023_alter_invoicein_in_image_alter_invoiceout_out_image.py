# Generated by Django 4.0.3 on 2022-06-06 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dnamservices', '0022_alter_invoicein_delete_alter_invoiceout_delete'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoicein',
            name='in_image',
            field=models.ImageField(upload_to='Invoice_in'),
        ),
        migrations.AlterField(
            model_name='invoiceout',
            name='out_image',
            field=models.ImageField(upload_to='Invoice_out'),
        ),
    ]
