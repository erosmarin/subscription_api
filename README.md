# Subscription API for Newsletter Service
This API system is designed to support a subscription-based feature for a newsletter service. Users can configure and create a subscription to receive newsletters tailored to their preferences. The configuration options include industry/sector, source, and subcategory.

# Set up
download the repo.
Create a virtual environment and install the required python packages.

```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

make initial migrations
```
python manage.py makemigrations
python manage.py migrate
```

run server
```
python manage.py runserver
```


# API Endpoints
1. Subscribe Endpoint
URL: /api/subscribe/
Method: POST
Description: This endpoint allows users to subscribe to the newsletter service.

Request Body:
```
json
{
    "email": "user@example.com",
    "industry": ["consumer_health"],
    "source": ["social_media"],
    "subcategory": ["new_product_releases"]
}
```

email (string, required): The email address of the user subscribing to the newsletter.
industry (string, required): The industry or sector the user is interested in (e.g., Consumer Health, Beauty, Tech).
source (string, required): The source from where the user prefers to receive content (e.g., Social Media, News).
subcategory (string, required): The subcategory of content the user is interested in (e.g., New Product Releases, Mergers and Acquisitions).

see apps/newsletter
Response:
200 OK: Successful subscription.
400 Bad Request: Invalid request body or missing required fields.