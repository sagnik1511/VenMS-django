from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="Home"),
    path("vendors/", views.vendors, name="Vendors"),
    path(
        "vendors/<int:vendor_code>/",
        views.get_or_update_vendor,
        name="get_vendor_details",
    ),
    path("purchase_orders/", views.purchase_orders, name="Purchase Orders"),
    path(
        "purchase_orders/<int:po_id>/",
        views.get_or_update_purchase_orders,
        name="get_po_details",
    ),
    path(
        "vendors/<int:vendor_id>/performance",
        views.get_vendor_metrics,
        name="Vendor Mentrics",
    ),
    path(
        "purchase_orders/<int:po_id>/acknowledge", views.acknowledge, name="Acknowledge"
    ),
]
