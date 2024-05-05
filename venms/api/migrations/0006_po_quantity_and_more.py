# Generated by Django 4.2.11 on 2024-05-05 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_remove_histperformance_fulfillment_rate_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='po',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
        migrations.RemoveField(
            model_name='histperformance',
            name='average_response_time',
        ),
        migrations.RemoveField(
            model_name='histperformance',
            name='fulfillment_rate',
        ),
        migrations.RemoveField(
            model_name='histperformance',
            name='on_time_delivery_rate',
        ),
        migrations.RemoveField(
            model_name='histperformance',
            name='quality_rating_avg',
        ),
        migrations.AddField(
            model_name='histperformance',
            name='average_response_time',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='histperformance',
            name='fulfillment_rate',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='histperformance',
            name='on_time_delivery_rate',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='histperformance',
            name='quality_rating_avg',
            field=models.FloatField(default=0),
        ),
    ]