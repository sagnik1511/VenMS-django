import json
import datetime as dt
from django.shortcuts import HttpResponse, get_object_or_404
from django.http import JsonResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from .models import Vendor, PO
from .backend_funcs import update_vendor_details

# Create your views here.


def home(request):
    return HttpResponse("HOME PAGE!", status=200)


@csrf_exempt
def vendors(request):
    if request.method == "GET":
        vendor_objs = Vendor.objects.all()
        vendor_list = [
            {field.name: getattr(vendor, field.name) for field in vendor._meta.fields}
            for vendor in vendor_objs
        ]
        return HttpResponse(vendor_list, status=200)
    elif request.method == "POST":
        try:
            data = json.loads(request.body)
        except:
            return HttpResponse("Inconsistent data posted", status=400)
        for field in ["name", "contact_details", "address", "vendor_code"]:
            if field not in data:
                return HttpResponse("Mandatory Fields missing", status=206)
            vendor = Vendor()
            if Vendor.objects.filter(vendor_code=int(data["vendor_code"])).exists():
                return HttpResponse("Vendor Id already occupied", status=409)
            for field in vendor._meta.fields:
                if field.name in data:
                    setattr(vendor, field.name, data[field.name])
        vendor.save()
        return HttpResponse("{} Added successfully!".format(data["name"]), status=201)
    else:
        return HttpResponse("Invalid request", status=405)


@csrf_exempt
def get_or_update_vendor(request, vendor_code):
    try:
        vendor = get_object_or_404(Vendor, vendor_code=vendor_code)
    except Http404 as e:
        return HttpResponse("Vendor Not Found", status=404)
    if request.method == "GET":
        vendor_data = {
            field.name: getattr(vendor, field.name) for field in vendor._meta.fields
        }
        return JsonResponse(vendor_data)
    elif request.method == "POST":
        try:
            data = json.loads(request.body)
        except:
            return HttpResponse("Inconsistent data posted", status=400)
        if "vendor_code" in data:
            return HttpResponse("Vendor code can't be changed", status=403)
        for field in vendor._meta.fields:
            if field.name in data:
                setattr(vendor, field.name, data[field.name])
        vendor.save()
        return HttpResponse("Vendor Details Updated Successfully", status=200)
    elif request.method == "DELETE":
        vendor.delete()
        return HttpResponse("Vendor Removed Successfully", status=200)
    else:
        return HttpResponse("Invalid request", status=405)


@csrf_exempt
def purchase_orders(request):
    if request.method == "GET":
        vendor_id = request.GET.get("vendor_id")
        if not vendor_id:
            return HttpResponse("Null Vendor Id", status=400)
        transactions = PO.objects.filter(vendor_id=vendor_id)
        if not transactions.exists():
            return HttpResponse(
                "No Records found for Vendor {}".format(vendor_id), status=404
            )
        transaction_list = [
            {
                field.name: getattr(transaction, field.name)
                for field in transaction._meta.fields
                if field.name != "vendor"
            }
            for transaction in transactions
        ]
        return HttpResponse(transaction_list, status=200)
    elif request.method == "POST":
        try:
            data = json.loads(request.body)
        except:
            return HttpResponse("Inconsistent data posted", status=400)
        for field in [
            "po_number",
            "vendor",
            "order_date",
            "delivery_date",
            "items",
            "status",
            "quality_rating",
            "issue_date",
        ]:
            if field not in data:
                return HttpResponse("Mandatory Fields missing", status=404)
            elif not data[field]:
                return HttpResponse("Mandatory Fields Blank", status=206)
        if not Vendor.objects.filter(vendor_code=int(data["vendor"])).exists():
            return HttpResponse("Vendor Id Not Present", status=404)
        po = PO()
        if PO.objects.filter(po_number=int(data["po_number"])).exists():
            return HttpResponse("PO Id Already Occupied", status=409)
        for field in po._meta.fields:
            if field.name in data:
                if field.name == "vendor":
                    vendor_obj = get_object_or_404(
                        Vendor, vendor_code=int(data["vendor"])
                    )
                    po.vendor = vendor_obj
                else:
                    setattr(po, field.name, data[field.name])
        po.save()
        update_vendor_details(po.po_number, data)
        return HttpResponse(
            "PO {} Added successfully!".format(data["po_number"]), status=200
        )
    else:
        return HttpResponse("Invalid request", status=405)


@csrf_exempt
def get_or_update_purchase_orders(request, po_id):
    try:
        po = get_object_or_404(PO, po_number=po_id)
    except Http404 as e:
        return HttpResponse("PO Not Found", status=404)
    if request.method == "GET":
        po_data = {}
        for field in po._meta.fields:
            if field.name != "vendor":
                po_data.update({field.name: getattr(po, field.name)})
            else:
                po_data.update({field.name: getattr(po, field.name).vendor_code})
        print(po_data)
        return JsonResponse(po_data)
    elif request.method == "POST":
        try:
            data = json.loads(request.body)
        except:
            return HttpResponse("Inconsistent data posted", status=400)
        if "po_number" in data:
            return HttpResponse("PO Number can't be updated")
        for field in po._meta.fields:
            if field.name in data:
                if field.name == "vendor":
                    if not Vendor.objects.filter(
                        vendor_code=int(data[field.name])
                    ).exists():
                        return HttpResponse("Vendor Id Not Present", status=404)
                    vendor_obj = get_object_or_404(
                        Vendor, vendor_code=int(data["vendor"])
                    )
                    po.vendor = vendor_obj
                else:
                    setattr(po, field.name, data[field.name])
        po.save()
        update_vendor_details(po_id, data)
        return HttpResponse("Vendor Details Updated Successfully", status=200)
    elif request.method == "DELETE":
        po.delete()
        return HttpResponse("PO {} deleted successfully".format(po_id))
    else:
        return HttpResponse("Invalid request", status=405)


def get_vendor_metrics(request, vendor_id):
    if request.method == "GET":
        try:
            vendor = get_object_or_404(Vendor, vendor_code=vendor_id)
        except:
            return HttpResponse("Vendor Not Found", status=404)
        metrics = {}
        for field in [
            "on_time_delivery_rate",
            "quality_rating_avg",
            "average_response_time",
            "fulfillment_rate",
        ]:
            metrics.update({field: getattr(vendor, field)})
        return JsonResponse(metrics)
    else:
        return HttpResponse("Invalid request", status=405)


@csrf_exempt
def acknowledge(request, po_id):
    if request.method == "POST":
        try:
            po = get_object_or_404(PO, po_number=po_id)
        except:
            return HttpResponse("Vendor Not Found", status=404)
        po.acknowledgement_date = dt.datetime.now()
        po_data = {
            "acknowledgement_date": po.acknowledgement_date.strftime(
                "%Y-%m-%d %H:%M:%S"
            )
        }
        po.save()
        update_vendor_details(po_id, po_data)
        return HttpResponse("Purchase Order Acknowledged", status=200)
    else:
        return HttpResponse("Invalid request", status=405)
