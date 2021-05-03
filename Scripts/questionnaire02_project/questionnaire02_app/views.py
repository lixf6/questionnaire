from django.shortcuts import render
from .models import Question


# Create your views here.
def base(request):
    question_list = Question.objects.all()
    return render(request, 'list.html', context={'question_list': question_list})
    # return render(request, 'list.html')