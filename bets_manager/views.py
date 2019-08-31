from django.shortcuts import render


def index(request):
    return render(request, 'bets_manager/index.html')


def about(request):
    return render(request, 'bets_manager/about.html')