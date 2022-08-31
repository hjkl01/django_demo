from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin

# Register your models here.
from apps.news_others.models import NewsOthers

# admin.site.site_header = "新闻others管理"
# admin.site.site_title = "新闻others管理"
# admin.site.index_title = "新闻others管理"


@admin.register(NewsOthers)
class NewsAdmin(ImportExportActionModelAdmin):

    list_display = [
        "id",
        "url",
        "website",
        "title",
        "filename",
        "if_sended",
        "created_time",
    ]
    search_fields = list_display
    list_filter = ("url", "website", "title", "filename")
    ordering = ("-created_time",)
    list_per_page = 20
    date_hierarchy = "created_time"
