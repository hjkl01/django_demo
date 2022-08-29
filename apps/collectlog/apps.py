from django.apps import AppConfig


class CollectlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.collectlog'
    verbose_name = "日志管理"
