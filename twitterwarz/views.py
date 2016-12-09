from django.shortcuts import render, HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the twitterwarz index.")

def test(request):
    return HttpResponse('My second view')
