from django.template.backends import django
from django_filters import FilterSet
from .models import Advertisement
from django import forms


class AdvertisementFilter(FilterSet):
    class Meta:

        model = Advertisement

        fields = {'category',
                  }