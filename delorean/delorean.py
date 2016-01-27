#!/usr/bin/env python
# encoding: utf-8

" A delorean module in python"


from datetime import date, datetime
import time


class Delorean(object):
    """A delorean class"""
    def __init__(self):
        super(Delorean, self).__init__()
        self.speed = 0
        self.plutonium = False
        self.date = datetime.now().date()
        self.target_date = None

    def set_speed(self, speed):
        "set the delorean speed"
        self.speed = speed
        self.__speed_changed()

    def get_speed(self):
        "return the delorean speed"
        return self.speed

    def insert_plutonium(self):
        "Insert plutonium in the reactor"
        self.plutonium = True

    @property
    def has_plutonium(self):
        "return True if there is plutonium"
        return self.plutonium

    def set_target_date(self, target_date):
        "Define the delorean target date, date shall follow format DD/MM/YYYY"
        self.target_date = datetime.strptime(target_date, '%d/%m/%Y').date()

    def get_date(self):
        "return the current delorean date location"
        return self.date

    def __speed_changed(self):
        "A callback to be called when speed change"
        if self.target_date is not None:
            if self.has_plutonium:
                if 88 < self.get_speed():
                    self.date = self.target_date
                    self.plutonium = False
                    print 'Delorean traveled in time to %s' % self.date.strftime('%d/%m/%Y')