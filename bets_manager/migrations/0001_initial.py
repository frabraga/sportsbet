# Generated by Django 2.2.4 on 2019-08-31 12:09

import bets_manager.fields
from decimal import Decimal
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SingleBet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('units', models.DecimalField(decimal_places=1, max_digits=10, validators=[django.core.validators.MinValueValidator(Decimal('0.1'))])),
                ('date', models.DateField()),
                ('match', models.CharField(max_length=255)),
                ('odds_in_decimal', models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(Decimal('1.01'))])),
                ('event', bets_manager.fields.EventField(choices=[('English Premier League', 'ENGLISH_PREMIER_LEAGUE'), ('Brasileirão Serie A', 'BRASILEIRAO_SERIE_A'), ('Brasileirão Serie B', 'BRASILEIRAO_SERIE_B'), ('Copa do Brasil', 'COPA_DO_BRASIL'), ('Copa Libertadores', 'COPA_LIBERTADORES'), ('Champions League', 'CHAMPIONS_LEAGUE')], max_length=255)),
                ('result', bets_manager.fields.ResultField(choices=[('won', 'WON'), ('won half', 'WON_HALF'), ('returned', 'RETURNED'), ('lost', 'LOST'), ('lost_half', 'LOST_HALF')], max_length=20)),
            ],
        ),
    ]
