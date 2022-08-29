from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin

# Register your models here.
from apps.news.models import News

admin.site.site_header = "新闻管理"
admin.site.site_title = "新闻管理"
admin.site.index_title = "新闻管理"


@admin.register(News)
class NewsAdmin(ImportExportActionModelAdmin):

    list_display = [
        "id",
        "url",
        "website",
        "title",
        "if_sended",
        "hot_score",
        "click_count",
        "created_time",
        "updated_time",
    ]
    search_fields = list_display
    list_filter = ("url", "website", "title", "if_sended", "hot_score", "click_count")
    ordering = ("-created_time",)
    list_per_page = 20
    date_hierarchy = "created_time"
