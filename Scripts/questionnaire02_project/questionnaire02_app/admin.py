from django.contrib import admin


# Register your models here.
from django.urls import reverse
from django.utils.html import format_html

from .models import Question, QuestionTitle


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    """后台问卷设置栏，admin/路径下"""
    list_display = [
        'title', 'created_time', 'question_count'
    ]

    list_filter = ['title', ]

    # 搜索栏中支持搜索字段
    search_fields = ['title']

    # actions_on_top = True
    # actions_on_bottom = True

    # 编辑页面
    save_on_top = True

    fields = (
        # ('category', 'title'),
        'title',
        'choice_one',
        'choice_two',
        'choice_three',
        'choice_four',
    )

    # 操作字段设置
    # def operator(self, obj):
    #     return format_html(
    #         '<a href="{}">编辑</a>',

    #     )
    # operator.short_description = '操作'

    def question_count(self, obj):
        """文章总数计数返回"""
        return 1  # 这里先占个位置，默认为1，后面需要更新统计值
    # 列表展示字段，该目录下对应文章字段展示名称
    question_count.short_description = "文章数量"

    # def save_model(self, request, obj, form, change):
    #     obj.owner = request.user
    #     return super(PostAdmin, self).save_model(request, obj, form, change)
    #
    # def get_queryset(self, request):
    #     qs = super(PostAdmin, self).get_queryset(request)
    #     return qs.filter(owner=request.user)

    # 继承bootstrap样式
    class Media:
        css = {
            'all': ("https://cdn.bootcss.com/bootstrap/4.0.0-beta.2/css/bootstrap.min.css",),
        }
        js = ('https://cdn.bootcss.com/bootstrap/4.0.0-beta.2/js/bootstrap.bundle.js',)


@admin.register(QuestionTitle)
class QuestionTitleAdmin(admin.ModelAdmin):
    """后台问卷设置栏，admin/路径下"""
    list_display = [
        'title', 'created_time'
    ]

    list_filter = ['title', ]

    # 搜索栏中支持搜索字段
    search_fields = ['title', ]

    # actions_on_top = True
    # actions_on_bottom = True

    # 编辑页面
    save_on_top = True

    # exclude = ['owner']
    fields = (
        # ('category', 'title'),
        'title',
        'introduction',
    )

    # 继承bootstrap样式
    class Media:
        css = {
            'all': ("https://cdn.bootcss.com/bootstrap/4.0.0-beta.2/css/bootstrap.min.css",),
        }
        js = ('https://cdn.bootcss.com/bootstrap/4.0.0-beta.2/js/bootstrap.bundle.js',)


# admin.site.register(Question, QuestionAdmin)