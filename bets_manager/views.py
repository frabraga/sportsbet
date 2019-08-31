from django.http import HttpResponseRedirect
from django.shortcuts import render

from bets_manager.choices import result_choices, events_choices
from bets_manager.models import SingleBet, sum_amount_won


def index(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            single_bet_attrs = {
                'date': request.POST['date'],
                'match': request.POST['match'],
                'odds_in_decimal': request.POST['odds'],
                'event': request.POST['event'],
                'result': request.POST['result'],
                'units': request.POST['units'],
                'detail': request.POST['detail'],
                'user': request.user
            }
            SingleBet.objects.create(**single_bet_attrs)
            return HttpResponseRedirect('/')

        bets = SingleBet.objects.filter(user=request.user)
        context = {
            'bets': bets,
            'events': events_choices,
            'result': result_choices,
            'sum_amount_won': sum_amount_won(request.user)
        }

        return render(request, 'bets_manager/index.html', context)

    return render(request, 'bets_manager/index.html')


def about(request):
    return render(request, 'bets_manager/about.html')
