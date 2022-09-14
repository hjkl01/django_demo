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

    # # 增加自定义按钮
    # actions = ["make_copy", "custom_button"]
    #
    # def custom_button(self, request, queryset):
    #     pass
    #
    # # 显示的文本，与django admin一致
    # custom_button.short_description = "测试按钮"
    # # icon，参考element-ui icon与https://fontawesome.com
    # custom_button.icon = "fas fa-audio-description"
    #
    # # 指定element-ui的按钮类型，参考https://element.eleme.cn/#/zh-CN/component/button
    # custom_button.type = "danger"
    #
    # # 给按钮追加自定义的颜色
    # custom_button.style = "color:black;"
    #
    # def make_copy(self, request, queryset):
    #     pass
    #
    # make_copy.short_description = "复制员工"
    # make_copy.confirm = 'are you sure?'
