import csv
import json
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dish_search.settings")
django.setup()

from dish_search_app.models import Restaurant

csv_file = 'restaurants_small.csv'

with open(csv_file, 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        items_available = json.loads(row['items'])
        full_details = row.get('full_details', '{}')
        try:
            full_details = json.loads(full_details)
        except json.JSONDecodeError:
            full_details = {}
        latitude_longitude = row['lat_long']
        restaurant = Restaurant(
            name=row['name'],
            location=row['location'],
            items_available=items_available,
            full_details=full_details,
            latitude_longitude=latitude_longitude
        )
        restaurant.save()
