
from rest_framework import viewsets
from tyadmin_api.custom import XadminViewSet
from django.contrib.auth.models import Permission, Group, User
from django.contrib.contenttypes.models import ContentType
from captcha.models import CaptchaStore
from tyadmin_api.models import TyAdminSysLog, TyAdminEmailVerifyRecord
from apps.news.models import News
from apps.collectlog.models import CollectLog

from tyadmin_api.auto_serializers import PermissionListSerializer, GroupListSerializer, UserListSerializer, ContentTypeListSerializer, CaptchaStoreListSerializer, TyAdminSysLogListSerializer, TyAdminEmailVerifyRecordListSerializer, NewsListSerializer, CollectLogListSerializer
from tyadmin_api.auto_serializers import PermissionCreateUpdateSerializer, GroupCreateUpdateSerializer, UserCreateUpdateSerializer, ContentTypeCreateUpdateSerializer, CaptchaStoreCreateUpdateSerializer, TyAdminSysLogCreateUpdateSerializer, TyAdminEmailVerifyRecordCreateUpdateSerializer, NewsCreateUpdateSerializer, CollectLogCreateUpdateSerializer
from tyadmin_api.auto_filters import PermissionFilter, GroupFilter, UserFilter, ContentTypeFilter, CaptchaStoreFilter, TyAdminSysLogFilter, TyAdminEmailVerifyRecordFilter, NewsFilter, CollectLogFilter

    
class PermissionViewSet(XadminViewSet):
    serializer_class = PermissionListSerializer
    queryset = Permission.objects.all().order_by('-pk')
    filter_class = PermissionFilter
    search_fields = ["name","codename"]

    def get_serializer_class(self):
        if self.action == "list":
            return PermissionListSerializer
        else:
            return PermissionCreateUpdateSerializer

    
class GroupViewSet(XadminViewSet):
    serializer_class = GroupListSerializer
    queryset = Group.objects.all().order_by('-pk')
    filter_class = GroupFilter
    search_fields = ["name"]

    def get_serializer_class(self):
        if self.action == "list":
            return GroupListSerializer
        else:
            return GroupCreateUpdateSerializer

    
class UserViewSet(XadminViewSet):
    serializer_class = UserListSerializer
    queryset = User.objects.all().order_by('-pk')
    filter_class = UserFilter
    search_fields = ["password","username","first_name","last_name","email"]

    def get_serializer_class(self):
        if self.action == "list":
            return UserListSerializer
        else:
            return UserCreateUpdateSerializer

    
class ContentTypeViewSet(XadminViewSet):
    serializer_class = ContentTypeListSerializer
    queryset = ContentType.objects.all().order_by('-pk')
    filter_class = ContentTypeFilter
    search_fields = ["app_label","model"]

    def get_serializer_class(self):
        if self.action == "list":
            return ContentTypeListSerializer
        else:
            return ContentTypeCreateUpdateSerializer

    
class CaptchaStoreViewSet(XadminViewSet):
    serializer_class = CaptchaStoreListSerializer
    queryset = CaptchaStore.objects.all().order_by('-pk')
    filter_class = CaptchaStoreFilter
    search_fields = ["challenge","response","hashkey"]

    def get_serializer_class(self):
        if self.action == "list":
            return CaptchaStoreListSerializer
        else:
            return CaptchaStoreCreateUpdateSerializer

    
class TyAdminSysLogViewSet(XadminViewSet):
    serializer_class = TyAdminSysLogListSerializer
    queryset = TyAdminSysLog.objects.all().order_by('-pk')
    filter_class = TyAdminSysLogFilter
    search_fields = ["ip_addr","action_flag","log_type","user_name"]

    def get_serializer_class(self):
        if self.action == "list":
            return TyAdminSysLogListSerializer
        else:
            return TyAdminSysLogCreateUpdateSerializer

    
class TyAdminEmailVerifyRecordViewSet(XadminViewSet):
    serializer_class = TyAdminEmailVerifyRecordListSerializer
    queryset = TyAdminEmailVerifyRecord.objects.all().order_by('-pk')
    filter_class = TyAdminEmailVerifyRecordFilter
    search_fields = ["code","email","send_type"]

    def get_serializer_class(self):
        if self.action == "list":
            return TyAdminEmailVerifyRecordListSerializer
        else:
            return TyAdminEmailVerifyRecordCreateUpdateSerializer

    
class NewsViewSet(XadminViewSet):
    serializer_class = NewsListSerializer
    queryset = News.objects.all().order_by('-pk')
    filter_class = NewsFilter
    search_fields = ["url","website","img_url"]

    def get_serializer_class(self):
        if self.action == "list":
            return NewsListSerializer
        else:
            return NewsCreateUpdateSerializer

    
class CollectLogViewSet(XadminViewSet):
    serializer_class = CollectLogListSerializer
    queryset = CollectLog.objects.all().order_by('-pk')
    filter_class = CollectLogFilter
    search_fields = ["hostname","extra","fileinfo","Function","Level","Module","name","Thread"]

    def get_serializer_class(self):
        if self.action == "list":
            return CollectLogListSerializer
        else:
            return CollectLogCreateUpdateSerializer
