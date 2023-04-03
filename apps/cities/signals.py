from django.db.models.signals import post_migrate
from django.dispatch import receiver
from apps.cities import models as m_cities

@receiver(post_migrate)
def create_cities(sender, **kwargs):
        cities_data = [
            {
                'name': 'New York',
                'latitude': 40.712776,
                'longitude': -74.005974,
            },
            {
                'name': 'London',
                'latitude': 51.507351,
                'longitude': -0.127758,
            },
            {
                'name': 'Paris',
                'latitude': 48.856613,
                'longitude': 2.352222,
            }
        ]

        for data in cities_data:
            m_cities.City.objects.get_or_create(**data)