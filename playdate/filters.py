from django_filters import rest_framework as filters
from .models import Playdate


class PlaydateFilter(filters.FilterSet):
    start_date = filters.DateFilter(field_name='date', lookup_expr='gte')
    end_date = filters.DateFilter(field_name='date', lookup_expr='lte')

    class Meta:
        model = Playdate
        fields = {
            'organizer': ['exact'],
            'title': ['icontains'],
            'location': ['icontains'],
            'parent_stay_required': ['exact'],
            'suitable_age': ['exact'],
            'date': ['exact', 'gte', 'lte'],
        }
