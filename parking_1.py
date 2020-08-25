#!/usr/bin/env python
# -*- coding: utf-8 -*-
# !@Time: 2020/8/12 16:58
# !@Author: Zhang-sl
class User(object):
    def __init__(self):
        self.user_ticket = 0

    def park(self, parkinglot):
        self.user_ticket = parkinglot.ticket
        print('parking success...')

    def take(self, parkinglot):
        if self.user_ticket == parkinglot.ticket:
            print('taking car success...')
            self.user_ticket = 0
        else:
            print('ticket is invalid...')


class ParkingLot(object):
    ticket = 1


