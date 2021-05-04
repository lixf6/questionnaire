from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Question, QuestionTitle, Answer


# Create your views here.
def base(request):
    """
    对应网址：http://127.0.0.1:8000
    见urls.py映射url路径
    :param request:
    :return:
    """
    question_list = Question.objects.all()  # 获取问题设置对应数据库信息
    questionTitle_list = QuestionTitle.objects.all()
    return render(request, 'list.html', context={'question_list': question_list,
                                                 'questionTitle_list': questionTitle_list})


def answer_input(request):
    """
    对应网址：http://127.0.0.1:8000/answer_input
    见urls.py映射url路径
    :param request:
    :return:
    """
    if request.method == 'POST':
        # tip = False
        form = request.POST  # request.POST为前端post表单传参的所有值
        answer = Answer()  # 初始化Answer模型实例，用来存储到数据库时用
        answer.body = form  # 将form提交过来的request对应的QueryDict值存到body中
        answer.save()  # 存到数据库Answer对应的表
        # print("answer_input提交的内容是：", form)
        # tip = True
        # return tip

    # reverses是根据urls.py中name='base'找到对应的url，从而找到对应的视图
    return HttpResponseRedirect(reverse('base'))
    # return render(request, 'list.html')
