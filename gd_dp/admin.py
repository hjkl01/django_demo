from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin

# Register your models here.
from gd_dp.models import ShopDetail

admin.site.site_header = "点评数据"
admin.site.site_title = "点评数据管理后台"
admin.site.index_title = "数据中心"


# admin.site.register(ShopDetail)
@admin.register(ShopDetail)
class ShopsTasksAdmin(ImportExportActionModelAdmin):

    list_display = [
        "shopname",
        "origin_shopname",
        "city",
        "district",
        "comments",
        "avg_price",
        "shop_cate",
        "create_time",
    ]
    search_fields = list_display
    list_filter = ("origin_shopname", "shopname", "city")
    ordering = ("-create_time",)
    list_per_page = 20
    date_hierarchy = "create_time"
