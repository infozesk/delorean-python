#!/usr/bin/env python
# encoding: utf-8

" Nom de Zeus marty !"

from delorean.delorean import Delorean

print 'Doc construit une delorean'
delo = Delorean()
print 'Nous sommes le %s' % delo.get_date()


print 'Doc refait le plein de plutonium'
delo.insert_plutonium()

print 'Doc programme un voyage dans le temps pour retourner en 1955'
delo.set_target_date('05/11/1955')

print 'Doc accelere jusqu a 89mph'
delo.set_speed(89)

print '####### VOYAGE DANS LE TEMPS #########'
print 'Nous sommes le %s' % delo.get_date()
