Here's a Markdown-formatted description of how to run the Vendor Management System API:


## How to Run the Vendor Management System API

### 1. Set Up Django Project

Ensure you have a Django project set up with the necessary files and configurations.

### 2. Database Configuration

Configure your database settings in the Django project's `settings.py` file.

### 3. Define Models

Define the `Vendor`, `PO`, and `HistoricalPerformance` models in the Django project's `models.py` file.

### 4. Create Views

Create views for handling various API endpoints. You can use the provided views in your Django project.

### 5. Define URLs

Define URL patterns for the API endpoints in the Django project's `urls.py` file.

### 6. Run Migrations

Run the following commands to create and apply database migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

### 7. Run Server

Start the Django development server by running:

```bash
python manage.py runserver
```

### 8. Test API Endpoints

Use tools like Postman or curl to test the API endpoints defined in the Django project.

### 9. (Optional) Document API

Document the API endpoints using tools like Swagger or Django Rest Framework's browsable API.

### 10. (Optional) Deploy

Deploy the Django project to a production environment if needed.

That's it! You should now be able to run the Vendor Management System API and interact with it using the defined endpoints.


#### Please Note
The SECRET_KEY in the `venms/venms/settings.py` has been removed. Please update your key there. Thanks.