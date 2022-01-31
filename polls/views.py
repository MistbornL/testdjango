from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def detail(request, question_id):
    return HttpResponse(f"Youre looking at question {question_id}")


def results(requests, question_id):
    response = f"Youre looking at response of question {question_id}"
    return HttpResponse(response)


def vote(requests, question_id):
    return HttpResponse(f"Youre voting on question {question_id}")
