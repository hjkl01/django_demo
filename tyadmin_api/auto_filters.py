from django_filters import rest_framework as filters
from tyadmin_api.custom import DateFromToRangeFilter
from django.contrib.auth.models import Permission, Group, User
from django.contrib.contenttypes.models import ContentType
from collectLog.models import CollectLog

class PermissionFilter(filters.FilterSet):
    content_type_text = filters.CharFilter(field_name="content_type")

    class Meta:
        model = Permission
        exclude = []

class GroupFilter(filters.FilterSet):

    class Meta:
        model = Group
        exclude = []

class UserFilter(filters.FilterSet):
    last_login = DateFromToRangeFilter(field_name="last_login")
    date_joined = DateFromToRangeFilter(field_name="date_joined")

    class Meta:
        model = User
        exclude = []

class ContentTypeFilter(filters.FilterSet):

    class Meta:
        model = ContentType
        exclude = []

class CollectLogFilter(filters.FilterSet):
    insert_time = DateFromToRangeFilter(field_name="insert_time")
    created_time = DateFromToRangeFilter(field_name="created_time")

    class Meta:
        model = CollectLog
        exclude = []