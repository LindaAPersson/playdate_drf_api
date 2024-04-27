from django_filters import rest_framework as filters
from .models import Playdate


class PlaydateFilter(filters.FilterSet):
    """
    Filter set class for the Playdate model.

    Attributes:
        start_date (DateFilter): Filter for playdates starting on or after a certain date.
        end_date (DateFilter): Filter for playdates ending on or before a certain date.
    """
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
