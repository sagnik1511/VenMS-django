# Generated by Django 4.2.11 on 2024-05-04 06:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('name', models.CharField(max_length=30)),
                ('contact_details', models.TextField(max_length=100)),
                ('address', models.TextField(max_length=200)),
                ('vendor_code', models.AutoField(primary_key=True, serialize=False)),
                ('on_time_delivery_rate', models.FloatField(default=0)),
                ('quality_rating_avg', models.FloatField(default=0)),
                ('average_response_time', models.FloatField(default=0)),
                ('fulfillment_rate', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='PO',
            fields=[
                ('po_number', models.AutoField(primary_key=True, serialize=False)),
                ('order_date', models.DateTimeField()),
                ('deliver_date', models.DateTimeField()),
                ('items', models.JSONField()),
                ('status', models.CharField(choices=[('P', 'Pending'), ('CM', 'Completed'), ('CN', 'Cancelled')], max_length=2)),
                ('quality_rating', models.FloatField(blank=True)),
                ('issue_date', models.DateTimeField()),
                ('acknowledgement_date', models.DateTimeField(blank=True)),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.vendor')),
            ],
        ),
        migrations.CreateModel(
            name='HistPerformance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('on_time_delivery_rate', models.FloatField()),
                ('quality_rating_avg', models.FloatField()),
                ('average_response_time', models.FloatField()),
                ('fulfillment_rate', models.FloatField()),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.vendor')),
            ],
        ),
    ]