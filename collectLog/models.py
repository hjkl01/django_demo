from django.db import models

# Create your models here.


class CollectLog(models.Model):

    id = models.AutoField(primary_key=True)
    elapsed = models.FloatField(verbose_name="消耗时间")
    exception = models.TextField(blank=True, null=True, verbose_name="异常")
    extra = models.CharField(max_length=200, verbose_name="其他")
    fileinfo = models.CharField(max_length=100, verbose_name="文件")
    functioN = models.CharField(max_length=100, verbose_name="函数名")
    leveL = models.CharField(max_length=10, verbose_name="等级信息")
    line = models.IntegerField(verbose_name="行数")
    message = models.TextField(verbose_name="信息")
    modulE = models.CharField(max_length=100, verbose_name="模块")
    name = models.CharField(max_length=100)
    procesS = models.BigIntegerField(verbose_name="进程信息")
    threaD = models.CharField(max_length=100, verbose_name="线程信息")
    insert_time = models.DateTimeField(verbose_name="log打印时间")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    # import django.utils.timezone
    # create_time = models.DateTimeField(default=django.utils.timezone.now, verbose_name="创建时间")
    # auto_now=True,  # 每次更新数据时更新
    # auto_now_add=True,  # 第一次插入数据时更新

    def __str__(self):
        return f"{self.leveL} {self.message}"

    class Meta:
        ordering = ["created_time"]
        db_table = "collectLog"
        verbose_name = "log日志"
        verbose_name_plural = "log日志"
        unique_together = ("created_time", "message")
