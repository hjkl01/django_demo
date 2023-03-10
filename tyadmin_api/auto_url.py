from tyadmin_api import auto_views
from django.urls import re_path, include, path
from rest_framework.routers import DefaultRouter
    
router = DefaultRouter(trailing_slash=False)
    
router.register('permission', auto_views.PermissionViewSet)
    
router.register('group', auto_views.GroupViewSet)
    
router.register('user', auto_views.UserViewSet)
    
router.register('content_type', auto_views.ContentTypeViewSet)
    
router.register('captcha_store', auto_views.CaptchaStoreViewSet)
    
router.register('ty_admin_sys_log', auto_views.TyAdminSysLogViewSet)
    
router.register('ty_admin_email_verify_record', auto_views.TyAdminEmailVerifyRecordViewSet)
    
router.register('news', auto_views.NewsViewSet)
    
router.register('collect_log', auto_views.CollectLogViewSet)
    
urlpatterns = [
        re_path('^', include(router.urls)),
    ]
    