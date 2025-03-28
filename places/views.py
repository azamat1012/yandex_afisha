from .models import Place, Image

import json

from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import JsonResponse
from django.urls import reverse


def fetch_places_data(request):
    places = Place.objects.all()

    geojson_container = {
        'type': 'FeatureCollection',
        'features': []
    }

    feature = [
        {
            'type': 'Feature',
            'geometry': {
                'type': 'Point',
                'coordinates': [place.longitude, place.latitude]
            },
            'properties': {
                'title': place.title,
                'placeId': place.id,
                'detailsUrl': reverse('place_detail', args=[place.id])
            }

        }
        for place in places
    ]
    geojson_container = {
        'type': 'FeatureCollection',
        'features': feature
    }

    geojson_data = json.dumps(geojson_container)
    context = {'geojson_data': geojson_data}
    return render(request, 'index.html', context=context)


def place_detail(request, id):
    place = get_object_or_404(Place.objects.prefetch_related('images'), id=id)
    images = place.images.all()

    places_data = {
        'title': place.title,
        'imgs': [img.image.url for img in images],
        'description_short': place.short_description,
        'description_long': place.long_description,
        'coordinates': {
            'lat': place.latitude,
            'lng': place.longitude
        }
    }

    return JsonResponse(places_data, json_dumps_params={'ensure_ascii': False, 'indent': 2})
