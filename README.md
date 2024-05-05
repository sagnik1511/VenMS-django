# Vendor Management System API

This API documentation provides information about managing vendors and purchase orders in a Vendor Management System.

## API Endpoints

### Home Page

- **GET /**: Returns the home page.

### Vendors

- **GET /vendors/**: Retrieves a list of all vendors.
- **POST /vendors/**: Creates a new vendor.
- **GET /vendors/{vendor_code}/**: Retrieves details of a specific vendor.
- **POST /vendors/{vendor_code}/**: Updates details of a specific vendor.
- **DELETE /vendors/{vendor_code}/**: Deletes a specific vendor.

### Purchase Orders

- **GET /purchase_orders/**: Retrieves purchase orders by vendor ID.
- **POST /purchase_orders/**: Creates a new purchase order.
- **GET /purchase_orders/{po_id}/**: Retrieves details of a specific purchase order.
- **POST /purchase_orders/{po_id}/**: Updates details of a specific purchase order.
- **DELETE /purchase_orders/{po_id}/**: Deletes a specific purchase order.

### Vendor Metrics

- **GET /vendors/{vendor_id}/performance**: Retrieves performance metrics of a specific vendor.

### Acknowledge Purchase Order

- **POST /purchase_orders/{po_id}/acknowledge**: Acknowledges a specific purchase order.

## Data Models

### Vendor

- `name`: string
- `contact_details`: string
- `address`: string
- `vendor_code`: integer
- `on_time_delivery_rate` : float
- `quality_rating_avg` : float
- `average_response_time` : float -> In seconds
- `fulfillment_rate` : float

### Purchase Order

- `po_number`: integer
- `vendor`: integer
- `order_date`: date-time
- `delivery_date`: date-time
- `items`: string
- `status`: string
- `quality_rating`: number
- `issue_date`: date-time

### Vendor Historical Performance 

- `vendor` : integer
- `date` : date-time
- `on_time_delivery_rate` : float
- `quality_rating_avg` : float
- `average_response_time` : float -> In seconds
- `fulfillment_rate` : float

## Getting Started

To use this API, follow the provided endpoints and make requests accordingly. You can use tools like Postman or curl to interact with the API endpoints.

## License

This project is licensed under the [MIT License](LICENSE).

## Installation

Please refere -> [install.md](https://github.com/sagnik1511/VenMS-django/blob/main/installation.md)


### Created using django and hyperactive weekends.
