from django.db import models

#  import django.utils.timezone


class NewsOthers(models.Model):

    id = models.AutoField(primary_key=True, verbose_name="唯一ID")
    url = models.URLField(null=False, unique=True, db_index=True, verbose_name="链接地址")
    website = models.CharField(max_length=100, null=True, blank=True, db_index=True, verbose_name="网站名称")
    title = models.TextField(null=False, verbose_name="标题")
    hot_score = models.IntegerField(default=0, verbose_name="热度")
    img_url = models.URLField(null=True, blank=True, verbose_name="图片地址")
    filename = models.TextField(null=False, blank=True, verbose_name="文件路径")

    if_sended = models.IntegerField(default=0, verbose_name="是否已发送")

    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    updated_time = models.DateTimeField(auto_now_add=True, verbose_name="更新时间")

    def to_dict(self):
        result = {}
        result["id"] = self.id
        result["url"] = self.url
        result["title"] = self.title
        result["created_time"] = self.created_time
        result["success"] = True
        return result

    def __str__(self):
        return f"{self.title} "

    class Meta:
        ordering = ["-created_time"]
        db_table = "data_news_others"
        verbose_name = "news"
        verbose_name_plural = "news"
        #  unique_together = ("origin_shopname", "shopname")
