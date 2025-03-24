import requests
import sys
import time
from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile
from places.models import Place, Image


class Command(BaseCommand):
    help = 'Loading the data via url'

    def add_arguments(self, parser):
        parser.add_argument("json_url", type=str, help="URL of the JSON file")

    def handle(self, *args, **options):
        json_url = options['json_url']
        try:
            response = requests.get(json_url)
            response.raise_for_status()
            place_data = response.json()

            place, created = Place.objects.update_or_create(
                title=place_data.get('title'),
                defaults={
                    'short_description': place_data.get('description_short'),
                    'long_description': place_data.get('description_long'),
                    'longitude': place_data['coordinates'].get('lng'),
                    'latitude': place_data['coordinates'].get('lat')
                }
            )

            image_urls = place_data.get('imgs', [])
            for i, image_url in enumerate(image_urls):
                try:
                    image_response = requests.get(
                        image_url, timeout=10)
                    image_response.raise_for_status()
                    Image.objects.create(
                        place=place,
                        image=ContentFile(
                            image_response.content, name=image_url.split('/')[-1])
                    )

                except requests.exceptions.HTTPError as e:
                    self.stderr.write(self.style.ERROR(
                        f"HTTP Error for image {i+1} ({image_url}): {e}"))
                except requests.exceptions.ConnectionError as e:
                    self.stderr.write(self.style.ERROR(
                        f"Error {e}"))
                    time.sleep(5)
                except Exception as e:
                    self.stderr.write(self.style.ERROR(
                        f"Error: {e}"))

            self.stdout.write(self.style.SUCCESS("Done!"))
        except requests.RequestException as e:
            self.stderr.write(self.style.ERROR(
                f"Error:{e}"))
            raise
