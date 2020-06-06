# -*- coding: utf-8 -*-

class Restriction_Hour():

    schedule_from = ''
    schedule_to = ''

    def __init__(day, schedule_from, schedule_to):
        
        self.schedule_from = ''
        self.schedule_to = ''

class Restriction_Day():
    day = ''
    schedule = False
    number_restricted = []

    def __init__(day, schedule, number_restricted):
        self.day = day
        self.schedule = schedule
        self.number_restricted = number_restricted
