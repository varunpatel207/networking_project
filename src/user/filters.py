from django_filters.rest_framework import FilterSet, CharFilter
from user.models import User


class UserFilterSet(FilterSet):
    username = CharFilter('email', label='email', lookup_expr='icontains')

    class Meta:
        model = User
        fields = ('username',)
