from django.contrib import admin


# Register your models here.
from django.urls import reverse
from django.utils.html import format_html

from .models import Question, QuestionTitle, Answer


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    """后台问卷设置栏，admin/路径下"""
    list_display = [
        'title', 'created_time',
        'choice_one', 'choice_two', 'choice_three', 'choice_four',
        'rate_choice_one',
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

    def rate_choice_one(self, obj):
        """用户投票计数返回"""
        import json
        ans_QuerySet = Answer.objects.values('body')  # 返回QuerySet对象，是一个类对象，可以迭代
        question_count = Question.objects.all().count()  # 返回一共有多少个问题

        ans_lst = []  # 用来存储所有问题的选型情况，即子集为所有下文中ans_dict_one的累加
        # 将问题展开为列表模式，主要是为了匹配数据库存储值，使得方便遍历时命中值
        question_choice = ['question'+ str(i) + '_choice' for i in range(1, question_count+1)]

        # print(question_count, question_choice)
        # print("ans_set:1111111", ans_QuerySet, type(ans_QuerySet))
        for question_choice_item in question_choice:
            ans_dict_one = {}  # 定义一个字典用来存储问题1的选择情况
            for ans in ans_QuerySet:
                ans_dict = ans['body'][12:-1]  # 把头尾非{}内容的str值去掉
                # 这里要注意，必须要把dict键的单引号换成双引号，否则会报错
                ans_dict = json.loads(ans_dict.replace("'", "\""))

                ans_dict_question_choice = ans_dict[question_choice_item][0]  # 去掉['choice_one']的括号
                # 借助字典dict.get计数统计，默认初始为0，也就是说一开始不存在该键值对时初始化为0
                ans_dict_one[ans_dict_question_choice] = ans_dict_one.get(ans_dict_question_choice, 0) + 1
            ans_lst.append(ans_dict_one)  # 每轮遍历完，可以依次得到问题1的所有选择，依次为问题2等，存到列表中
        # print(ans_lst)
        return ans_lst  # 返回所有的用户回复问题的所有选择统计值
    # 列表展示字段，该目录下对应文章字段展示名称
    rate_choice_one.short_description = "所有用户问卷反馈结果"
    # 操作字段设置
    # def operator(self, obj):
    #     return format_html(
    #         '<a href="{}">编辑</a>',

    #     )
    # operator.short_description = '操作'

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
        'title', 'question_ans_count', 'created_time'
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

    def question_ans_count(self, obj):
        """文章总数计数返回"""
        ans_count = Answer.objects.all().count()
        return ans_count  # 这里先占个位置，默认为1，后面需要更新统计值
    # 列表展示字段，该目录下对应文章字段展示名称
    question_ans_count.short_description = "问卷回复数量"

    # 继承bootstrap样式
    class Media:
        css = {
            'all': ("https://cdn.bootcss.com/bootstrap/4.0.0-beta.2/css/bootstrap.min.css",),
        }
        js = ('https://cdn.bootcss.com/bootstrap/4.0.0-beta.2/js/bootstrap.bundle.js',)


# admin.site.register(Question, QuestionAdmin)