from django.db import models


# Create your models here.
class Question(models.Model):
    """问卷数据库模型"""
    title = models.CharField(max_length=255, verbose_name="问卷标题")
    # content = models.TextField(verbose_name="正文")  # 留着以后扩展用
    choice_one = models.CharField(max_length=255, verbose_name="默认选择1")
    choice_two = models.CharField(max_length=255, verbose_name="默认选择2")
    choice_three = models.CharField(max_length=255, verbose_name="默认选择3")
    choice_four = models.CharField(max_length=255, verbose_name="默认选择4")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    class Meta:
        """它的作用是配置 Model属性，比如 Question 这个
        Model 通过 Meta 配置它的展示名称为调查问卷，排序规 是根据 id 降序排列"""
        verbose_name = verbose_name_plural = "调查问卷"
        # ordering = ['-id']

    def __str__(self):
        return self.title
