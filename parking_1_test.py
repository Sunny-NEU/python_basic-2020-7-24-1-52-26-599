#!/usr/bin/env python
# -*- coding: utf-8 -*-
# !@Time: 2020/8/12 17:32
# !@Author: Zhang-sl
import unittest
from parking_1 import ParkingLot, User


class parking_1_test(unittest.TestCase):
    def test_park(self):
        pl = ParkingLot()
        user = User()
        user.park(pl)
        self.assertTrue(user.user_ticket)
        user.take(pl)
        self.assertFalse(user.user_ticket)
        user.take(pl)
        self.assertFalse(user.user_ticket)

if __name__ == '__main__':
    unittest.main()
