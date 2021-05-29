import django_filters
from souq.models import Souq




class SouqFilter(django_filters.FilterSet):
    manufacture = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Souq
        fields = ['manufacture', 'category']