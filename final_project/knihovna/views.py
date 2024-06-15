from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import Uzivatel, Hra


def index(request):
    hry = Hra.objects.all()
    return render(request, 'index.html', {'hry': hry})


def list_users(request):
    hry = Hra.objects.all()
    users = Uzivatel.objects.all().values()
    return render(request, 'list_users.html', {'hry': hry, 'users': users})


def list_games(request):
    hry = Hra.objects.all()
    return render(request, 'list_games.html', {'hry': hry})


def user(request, id):
    users = Uzivatel.objects.get(id=id)
    return render(request, 'user.html', {'users': users})


def game(request, id):
    hry = Hra.objects.get(id=id)
    return render(request, 'game.html', {'hry': hry})





