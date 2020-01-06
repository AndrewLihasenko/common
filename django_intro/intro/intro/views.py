import requests
from django.http import HttpResponse
from django.shortcuts import render

USER_URL = 'https://api.github.com/users/'


def health_check(request):
    return HttpResponse("OK")


def index(request):
    return HttpResponse(render(request, 'base.html'))


def github(request):
    user = {}
    if 'username' in request.GET:
        username = request.GET['username']
        response = requests.get(f'{USER_URL}%s' % username)
        user = response.json()
    return render(request, 'github.html', {'user': user})
