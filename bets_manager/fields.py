from django.db import models

from bets_manager.enum import SportsEventEnum, ResultEnum


class EventField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('max_length', 255)
        kwargs.setdefault('choices', SportsEventEnum.get_choices())
        super().__init__(*args, **kwargs)


class ResultField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('max_length', 20)
        kwargs.setdefault('choices', ResultEnum.get_choices())
        super().__init__(*args, **kwargs)
