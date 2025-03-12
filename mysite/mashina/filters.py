from django_filters import FilterSet
from .models import *

class CarFilter(FilterSet):
    class Meta:
        model = Car
        fields = {
            'year': ['gt', 'lt'],
            'price': ['gt', 'lt'],
        }