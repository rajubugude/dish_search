from django.shortcuts import render
from .models import Restaurant
import json

def search(request):
    if request.method == 'POST':
        query = request.POST.get('query', '')
        restaurants = Restaurant.search_dish(query)
        processed_restaurants = process_restaurants(restaurants, query)
        return render(request, 'search.html', {'restaurants': processed_restaurants, 'query': query})
    
    return render(request, 'search.html')

def process_restaurants(restaurants, query):
    processed_restaurants = []
    processed_restaurant_names = set()  # Track processed restaurant names
    
    for restaurant in restaurants:
        processed_dishes = []
        items_available = restaurant.items_available
        for dish, price in items_available.items():
            if query.lower() in dish.lower():
                processed_dishes.append({'dish': dish, 'price': price})
        
        if processed_dishes:
            restaurant_name = restaurant.name
            if restaurant_name not in processed_restaurant_names:
                processed_restaurant_names.add(restaurant_name)
                processed_restaurants.append({'restaurant': restaurant, 'dishes': processed_dishes})

    return processed_restaurants




