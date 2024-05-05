# Generated by Django 4.2.11 on 2024-05-04 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_floatvalue_rename_deliver_date_po_delivery_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='histperformance',
            name='fulfillment_rate',
        ),
        migrations.AddField(
            model_name='histperformance',
            name='fulfillment_rate',
            field=models.ManyToManyField(related_name='fr_fl', to='api.floatvalue'),
        ),
    ]