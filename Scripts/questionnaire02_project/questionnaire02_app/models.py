from django.db import models


# Create your models here.
class Question(models.Model):
    """前端用户PC端查看问卷的问题及选择数据库模型"""
    title = models.CharField(max_length=255, verbose_name="问卷标题")
    # content = models.TextField(verbose_name="正文")  # 留着以后扩展用
    choice_one = models.CharField(max_length=255, verbose_name="默认选择1（A）")
    choice_two = models.CharField(max_length=255, verbose_name="默认选择2（B）")
    choice_three = models.CharField(max_length=255, verbose_name="默认选择3（C）")
    choice_four = models.CharField(max_length=255, verbose_name="默认选择4（D）")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    class Meta:
        """它的作用是配置 Model属性，比如 Question 这个
        Model 通过 Meta 配置它的展示名称为调查问卷，排序规 是根据 id 降序排列"""
        verbose_name = verbose_name_plural = "调查问卷-题目设置（目前只单选）"
        # ordering = ['-id']

    # def __str__(self):
    #     return self.title


class QuestionTitle(models.Model):
    """前端用户PC端查看问卷的顶部标题、背景介绍"""
    title = models.CharField(max_length=255, verbose_name="问卷顶部大标题")
    introduction = models.TextField(max_length=1024, verbose_name="问卷背景介绍")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    class Meta:
        """它的作用是配置 Model属性，比如 Question 这个
        Model 通过 Meta 配置它的展示名称为调查问卷，排序规 是根据 id 降序排列"""
        verbose_name = verbose_name_plural = "调查问卷-问卷背景介绍"
        # ordering = ['-id']

    def __str__(self):
        return self.title


class Answer(models.Model):
    """用户提交数据数据库存储模型"""
    body = models.TextField(max_length=1024, verbose_name="用户所有问题回答-字典设计")
    # author = models.CharField(max_length=255, verbose_name="提交人名称", required=False)
    # sex = models.CharField(max_length=255, verbose_name="提交人性别", required=False)
    # age = models.CharField(max_length=255, verbose_name="提交人年龄", required=False)
    # others = models.CharField(max_length=255, verbose_name="扩展字段", required=False)
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    class Meta:
        """它的作用是配置 Model属性，比如 Question 这个
        Model 通过 Meta 配置它的展示名称为调查问卷，排序规 是根据 id 降序排列"""
        verbose_name = verbose_name_plural = "调查问卷-用户提交问卷结果页"
        # ordering = ['-id']

    def __str__(self):
        return self.body