from django.db import models

#  import django.utils.timezone


class News(models.Model):

    id = models.AutoField(primary_key=True)
    # url = models.URLField(null=False, db_index=True)
    url = models.URLField(null=False, unique=True, db_index=True)
    website = models.CharField(max_length=100, null=True, blank=True, db_index=True)
    title = models.TextField(null=False)
    hot_score = models.IntegerField(default=0)
    img_url = models.URLField(null=True, blank=True)

    click_count = models.IntegerField(default=0)
    if_sended = models.IntegerField(default=0, verbose_name="if sended")

    # created_time = models.DateField(auto_now_add=True, verbose_name="创建时间")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    updated_time = models.DateTimeField(auto_now_add=True, verbose_name="date update")

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
        db_table = "spider_news"
        verbose_name = "news"
        verbose_name_plural = "news"
        #  unique_together = ("origin_shopname", "shopname")
