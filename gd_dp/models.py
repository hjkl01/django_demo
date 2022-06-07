from django.db import models
import django.utils.timezone


class ShopDetail(models.Model):

    id = models.AutoField(primary_key=True)
    appname = models.CharField(
        max_length=100,
        verbose_name="app名称",
        default="com.dianping.v1",
    )
    city = models.CharField(max_length=10)
    origin_shopname = models.CharField(max_length=100, verbose_name="原始店铺")
    shopname = models.CharField(max_length=100)
    district = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name="店铺所属区域",
    )
    max_dishes = models.IntegerField(blank=True, null=True, default=20)
    comments = models.CharField(max_length=10, verbose_name="评价人数")
    comment_score = models.CharField(max_length=10, verbose_name="评分")
    comment_detail = models.CharField(max_length=50, blank=True, null=True, verbose_name="评价详情")
    avg_price = models.CharField(max_length=20, verbose_name="均价")
    shop_cate = models.CharField(max_length=10, verbose_name="店铺所属分类")
    address = models.CharField(max_length=100, blank=True, null=True, verbose_name="店铺地址")
    address_detail = models.CharField(max_length=100, blank=True, null=True, verbose_name="店铺地址详情")
    phone = models.CharField(max_length=100, blank=True, null=True, verbose_name="电话")
    messages = models.TextField(blank=True, null=True, verbose_name="其他信息")
    dishes = models.JSONField(blank=True, null=True, verbose_name="推荐菜")

    create_time = models.DateTimeField(default=django.utils.timezone.now, verbose_name="创建时间")
    update_time = models.DateTimeField(
        auto_now_add=True,
        verbose_name="date update",
    )

    def to_dict(self):
        result = {}
        result["appname"] = self.appname
        result["city"] = self.city
        result["origin_shopname"] = self.origin_shopname
        result["shopname"] = self.shopname
        result["district"] = self.district
        result["max_dishes"] = self.max_dishes
        result["success"] = True
        return result

    def __str__(self):
        return f"{self.origin_shopname} {self.shopname}"

    class Meta:
        ordering = ["create_time"]
        db_table = "shop_detail_info"
        verbose_name = "店铺详细信息任务"
        verbose_name_plural = "店铺详细信息任务"
        unique_together = ("origin_shopname", "shopname")
