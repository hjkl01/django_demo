from django_filters import rest_framework as filters
from tyadmin_api.custom import DateFromToRangeFilter
from django.contrib.auth.models import Permission, Group, User
from django.contrib.contenttypes.models import ContentType
from captcha.models import CaptchaStore
from tyadmin_api.models import TyAdminSysLog, TyAdminEmailVerifyRecord
from apps.news.models import News
from apps.collectlog.models import CollectLog

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

class CaptchaStoreFilter(filters.FilterSet):
    expiration = DateFromToRangeFilter(field_name="expiration")

    class Meta:
        model = CaptchaStore
        exclude = []

class TyAdminSysLogFilter(filters.FilterSet):
    action_time = DateFromToRangeFilter(field_name="action_time")

    class Meta:
        model = TyAdminSysLog
        exclude = []

class TyAdminEmailVerifyRecordFilter(filters.FilterSet):
    send_time = DateFromToRangeFilter(field_name="send_time")

    class Meta:
        model = TyAdminEmailVerifyRecord
        exclude = []

class NewsFilter(filters.FilterSet):
    created_time = DateFromToRangeFilter(field_name="created_time")
    updated_time = DateFromToRangeFilter(field_name="updated_time")

    class Meta:
        model = News
        exclude = []

class CollectLogFilter(filters.FilterSet):
    insert_time = DateFromToRangeFilter(field_name="insert_time")
    created_time = DateFromToRangeFilter(field_name="created_time")

    class Meta:
        model = CollectLog
        exclude = []