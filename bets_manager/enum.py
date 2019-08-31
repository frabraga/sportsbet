from enum import Enum, unique


class EnumChoice(Enum):
    @classmethod
    def get_choices(cls):
        return [(a.value, a.name) for a in cls]


@unique
class SportsEventEnum(EnumChoice):
    ENGLISH_PREMIER_LEAGUE = 'English Premier League'
    BRASILEIRAO_SERIE_A = 'Brasileirão Serie A'
    BRASILEIRAO_SERIE_B = 'Brasileirão Serie B'
    COPA_DO_BRASIL = 'Copa do Brasil'
    COPA_LIBERTADORES = 'Copa Libertadores'
    CHAMPIONS_LEAGUE = 'Champions League'


@unique
class ResultEnum(EnumChoice):
    WON = 'won'
    WON_HALF = 'won_half'
    RETURNED = 'returned'
    LOST = 'lost'
    LOST_HALF = 'lost_half'
