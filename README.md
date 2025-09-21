# Django Datasets API

This project provides a complete CRUD (Create, Read, Update, Delete) API for managing datasets, built with Django and Django REST Framework, and secured with JWT authentication.

-----

## Setup Instructions

1.  **Prerequisites:**

      * Python 3.8+
      * `pip`

2.  **Set Up Virtual Environment and Install Dependencies:**

    ```bash
    # Create and activate a virtual environment
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

    # Install dependencies
    pip install django djangorestframework djangorestframework-simplejwt
    ```

3.  **Create Django Project and App:**

    ```bash
    django-admin startproject api_project
    cd api_project
    python manage.py startapp datasets
    ```

4.  **Add Files to the `datasets` App:**

      * Place the generated `models.py`, `serializers.py`, `views.py`, and `urls.py` into the `datasets/` directory.

5.  **Configure Project Settings:**

      * Open `api_project/settings.py`.
      * Add `rest_framework` and `datasets` to your `INSTALLED_APPS` list.
      * Add the `REST_FRAMEWORK` setting to configure JWT as the default authentication method.

    <!-- end list -->

    ```python
    INSTALLED_APPS = [
        # ... other apps
        'rest_framework',
        'datasets',
    ]

    REST_FRAMEWORK = {
        'DEFAULT_AUTHENTICATION_CLASSES': (
            'rest_framework_simplejwt.authentication.JWTAuthentication',
        )
    }
    ```

6.  **Configure Project URLs:**

      * Open `api_project/urls.py` and add the URLs for the `datasets` app and for JWT token authentication.

    <!-- end list -->

    ```python
    from django.contrib import admin
    from django.urls import path, include
    from rest_framework_simplejwt.views import (
        TokenObtainPairView,
        TokenRefreshView,
    )

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('api/', include('datasets.urls')),
        path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
        path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    ]
    ```

7.  **Create Database Migrations:**

      * Run the following commands to create the database table for your `Dataset` model.

    <!-- end list -->

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

8.  **Create a Superuser:**

      * You'll need a user to generate JWT tokens.

    <!-- end list -->

    ```bash
    python manage.py createsuperuser
    ```

      * Follow the prompts to create your admin user.

9.  **Run the Development Server:**

    ```bash
    python manage.py runserver
    ```

      * The API will be available at `http://127.0.0.1:8000/api/`.

-----

## API Endpoints & Samples

### Authentication

  * **Get Access and Refresh Tokens:**

      * `POST /api/token/`
      * **Body:** `{ "username": "your_username", "password": "your_password" }`
      * **Sample `curl` command:**
        ```bash
        curl -X POST http://127.0.0.1:8000/api/token/ \
        -H "Content-Type: application/json" \
        -d '{
            "username": "your_username",
            "password": "your_password"
        }'
        ```

  * **Refresh Access Token:**

      * `POST /api/token/refresh/`
      * **Body:** `{ "refresh": "your_refresh_token" }`

### Datasets

  * **List and Create Datasets:**

      * `GET /api/datasets/`
      * `POST /api/datasets/`
      * **Sample `curl` command (POST with authentication):**
        ```bash
        curl -X POST http://127.0.0.1:8000/api/datasets/ \
        -H "Authorization: Bearer <your_access_token>" \
        -H "Content-Type: application/json" \
        -d '{
            "data": {"details": "Violation detected"},
            "dataset_type": "speed_violation",
            "from_date": "2025-09-21T14:30:00Z",
            "to_date": "2025-09-21T14:35:00Z"
        }'
        ```

  * **Retrieve, Update, and Delete a Specific Dataset:**

      * `GET /api/datasets/{id}/`
      * `PUT /api/datasets/{id}/`
      * `PATCH /api/datasets/{id}/`
      * `DELETE /api/datasets/{id}/`

-----

## Authentication Flow

1.  **Obtain Tokens:** Send a `POST` request with your `username` and `password` to `/api/token/` to receive your initial `access` and `refresh` tokens.
2.  **Authenticate Requests:** For any request to a protected endpoint (like `/api/datasets/`), include the `access` token in the `Authorization` header. The format must be `Authorization: Bearer <your_access_token>`.
3.  **Refresh Token:** When your `access` token expires, you will receive an error. To get a new one, send a `POST` request containing your `refresh` token to the `/api/token/refresh/` endpoint.
