#!/usr/bin/env python
# encoding: utf-8

"""
tests the delorean module
"""

import datetime
import pytest
import delorean
from delorean import Delorean


def test_delorean():
    "Test the class initialisation"
    delo = Delorean()
    assert delo.get_speed() == 0
    assert delo.get_date() == datetime.date.today()
    assert delo.plutonium == False


def test_delorean_set_speed():
    "test the delorean set_speed method"
    delo = Delorean()
    assert delo.get_speed() == 0
    for speed in range(1,100):
        delo.set_speed(speed)
        assert delo.get_speed() == speed


def test_delorean_insert_plutonium():
    "test the delorean plutonium insertion"
    delo = Delorean()
    assert delo.has_plutonium == False
    delo.insert_plutonium()
    assert delo.has_plutonium == True


def test_delorean_target_date():
    "test the delorean plutonium insertion"
    delo = Delorean()
    assert delo.target_date is None
    delo.set_target_date('01/12/2199')
    assert delo.target_date == datetime.date(2199, 12, 01)
    delo.set_target_date('10/01/1200')
    assert delo.target_date == datetime.date(1200, 01, 10)


def test_delorean_get_date():
    "test the delorean plutonium insertion"
    delo = Delorean()
    assert delo.get_date() == datetime.date.today()


def test_delorean_time_travel():
    "test the time travel capabilities"
    delo = Delorean()
    today = datetime.date.today()
    assert delo.get_date() == today

    tomorrow = datetime.date(2199, 12, 01)
    delo.set_target_date('01/12/2199')
    # no time travel
    assert delo.get_date() == today

    # insert plutonium
    delo.insert_plutonium()
    # no time travel
    assert delo.get_date() == today

    # go below 88mph
    delo.set_speed(87)
    # no time travel
    assert delo.get_date() == today

    # go beyond 88mph
    delo.set_speed(89)
    assert delo.get_date() == tomorrow
    assert delo.has_plutonium == False
