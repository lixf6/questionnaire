from django.shortcuts import render
from .models import Question, QuestionTitle


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