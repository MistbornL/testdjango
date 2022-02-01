from django.http import HttpResponse
from django.template import loader

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    return HttpResponse(f"Youre looking at question {question_id}")


def results(requests, question_id):
    response = f"Youre looking at response of question {question_id}"
    return HttpResponse(response)


def vote(requests, question_id):
    return HttpResponse(f"Youre voting on question {question_id}")
