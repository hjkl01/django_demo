from django.contrib import admin

# Register your models here.

from import_export.admin import ImportExportActionModelAdmin


from collectLog.models import CollectLog

# admin.site.site_header = ""
# admin.site.site_title = "点评数据管理后台"
# admin.site.index_title = "数据中心"


# admin.site.register(ShopDetail)
@admin.register(CollectLog)
class CollectLogAdmin(ImportExportActionModelAdmin):

    list_display = [
        "id",
        "elapsed",
        "exception",
        "extra",
        "fileinfo",
        "functioN",
        "leveL",
        "line",
        "message",
        "modulE",
        "name",
        "procesS",
        "threaD",
        "insert_time",
        "created_time",
    ]
    search_fields = list_display
    list_filter = ("exception", "fileinfo", "functioN", "leveL", "line", 'modulE', 'procesS')
    ordering = ("-created_time",)
    list_per_page = 100
    date_hierarchy = "created_time"
