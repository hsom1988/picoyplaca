# -*- coding: utf-8 -*-

import car, schedule

from datetime import datetime, date

class Process():
    
    def __init__():
        pass

    def process_data(plate, date, time, restriction_schedule):
        # Creation of the car
        car = Car(plate)
        day_of_week = datetime.strptime(date, '%Y-%m-%d').weekday()
        time_received = datetime.strptime(date, '%H-%M').weekday()
        for restriction in restriction_schedule:
            if car.plate[-1] in restriction.number_restricted:
                if restriction.day == day_of_week:
                    if restriction.schedule.schedule_from >= time_received and restriction.schedule.schedule_to <= time_received:
                        return 'Usted no puede circular en la fecha %s a la hora %s'%(date, time)
        return 'Usted si puede circular el dia %s a las %s'%(date, time)
