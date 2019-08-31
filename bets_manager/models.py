from decimal import Decimal

from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.db import models
from bets_manager import fields
from bets_manager.enum import ResultEnum


class SingleBet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    units = models.DecimalField(
        decimal_places=1, max_digits=10,
        validators=[MinValueValidator(Decimal('0.1'))]
    )
    date = models.DateField()
    match = models.CharField(max_length=255)
    odds_in_decimal = models.DecimalField(
        decimal_places=2, max_digits=10,
        validators=[MinValueValidator(Decimal('1.01'))]
    )
    event = fields.EventField()
    result = fields.ResultField()

    @property
    def amount_won(self):
        if self.result == ResultEnum.RETURNED.value:
            return 0
        elif self.result == ResultEnum.WON.value:
            return self.units * self.odds_in_decimal - self.units
        elif self.result == ResultEnum.WON_HALF.value:
            return (self.units * self.odds_in_decimal - self.units) / 2
        elif self.result == ResultEnum.LOST.value:
            return -self.units
        elif self.result == ResultEnum.LOST_HALF.value:
            return -(self.units / 2)

    def __str__(self):
        return '{} - {}'.format(self.match, self.result)
