import json
import datetime as dt
from django.shortcuts import get_object_or_404


from .models import Vendor, PO, HistPerformance, FloatValue


def float_value(val):
    fl = FloatValue()
    fl.value = val

    return fl


def count_average(vendor: float, value_array: FloatValue):
    count = value_array.count()

    total_sum = sum([value.value for value in value_array])

    return total_sum / count


def count_average_efficient(vendor: float, value_array: FloatValue):
    count = value_array.count() - 1
    input_value = value_array.last()

    return (vendor * count + input_value) / (count + 1)


def update_vendor_details(vendor: Vendor, historical: HistPerformance):

    for field in [
        "on_time_delivery_rate",
        "quality_rating_avg",
        "average_response_time",
        "fulfillment_rate",
    ]:
        setattr(vendor, field, count_average_efficient(vendor.field, historical.field))

    vendor.save()


def update_vendor_details(po_id, curr_po_data):
    vendor = get_object_or_404(PO, po_number=po_id).vendor
    po = get_object_or_404(PO, po_number=po_id)
    vendor_metrics = {}
    hist = HistPerformance()
    if HistPerformance.objects.filter(vendor=vendor).exists():
        hist_perf = HistPerformance.objects.filter(vendor=vendor).last()

        # Copy current state to new histrical record
        for field in hist_perf._meta.fields:
            setattr(hist, field.name, getattr(hist_perf, field.name))

    total_po_count = PO.objects.filter(vendor=vendor).count()
    completed_po_count = PO.objects.filter(vendor=vendor, status="CM").count()

    hist.vendor = vendor
    hist.date = dt.datetime.now()

    if curr_po_data.get("acknowledgement_date"):
        # Calculating ART
        if total_po_count > 0:
            curr_time_diff = po.acknowledgement_date - po.issue_date
            art = (
                vendor.average_response_time * (total_po_count - 1)
                + curr_time_diff.seconds
            ) / total_po_count

            hist.average_response_time = art
            vendor_metrics.update({"average_response_time": art})

    if curr_po_data.get("status"):
        # Calculating FRA

        if total_po_count > 0:
            ffr = completed_po_count / total_po_count
            hist.fulfillment_rate = ffr
            vendor_metrics.update({"fulfillment_rate": ffr})

    if curr_po_data.get("status") == "CM":
        completed_po_count = PO.objects.filter(vendor=vendor, status="CM").count()

        # Calculating OTD rate

        curr_date = dt.date.today()
        otd_flag = curr_date <= po.delivery_date.date()
        otd_rate = (
            vendor.on_time_delivery_rate * (completed_po_count - 1) + int(otd_flag)
        ) / completed_po_count
        hist.on_time_delivery_rate = otd_rate
        vendor_metrics.update({"on_time_delivery_rate": otd_rate})

        if curr_po_data.get("quality_rating"):
            # Calculating QRA

            qra = (
                vendor.quality_rating_avg * (completed_po_count - 1)
                + curr_po_data.get("quality_rating")
            ) / completed_po_count
            hist.quality_rating_avg = qra
            vendor_metrics.update({"quality_rating_avg": qra})

    # Updating the metrics for latest results
    for field, value in vendor_metrics.items():
        setattr(vendor, field, value)

    vendor.save()
    hist.save()
