from django.db import models

# Create your models here.


class FloatValue(models.Model):
    value = models.FloatField()


class Vendor(models.Model):
    name = models.CharField(max_length=30)
    contact_details = models.TextField(max_length=100)
    address = models.TextField(max_length=200)
    vendor_code = models.CharField(max_length=10, primary_key=True)
    on_time_delivery_rate = models.FloatField(default=0)
    quality_rating_avg = models.FloatField(default=0)
    average_response_time = models.FloatField(default=0)
    fulfillment_rate = models.FloatField(default=0)

    def __str__(self):
        return self.vendor_code


class PO(models.Model):

    class StatusType(models.TextChoices):
        P = "P", "Pending"
        CM = "CM", "Completed"
        CN = "CN", "Cancelled"

    po_number = models.CharField(max_length=15, primary_key=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    order_date = models.DateTimeField()
    delivery_date = models.DateTimeField()
    items = models.JSONField()
    quantity = models.IntegerField(default=1)
    status = models.CharField(max_length=2, choices=StatusType.choices)
    quality_rating = models.FloatField(blank=True)
    issue_date = models.DateTimeField()
    acknowledgement_date = models.DateTimeField(blank=True)

    def __str__(self):
        return self.po_number


class HistPerformance(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    date = models.DateTimeField()
    on_time_delivery_rate = models.FloatField(default=0)
    quality_rating_avg = models.FloatField(default=0)
    average_response_time = models.FloatField(default=0)
    fulfillment_rate = models.FloatField(default=0)

    def __str__(self):
        return self.vendor
