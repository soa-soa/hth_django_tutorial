from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index. This is from the hth_django_tutorial folder.")

def detail(request, question_id):
    return HttpResponse("Your're looking at question %s." % question_id)

def results(request, question_id):
    response = "Your're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

