#!/usr/bin/env python
# -*- coding: utf-8 -*-
#!@Time: 2020/8/24 20:41
#!@Author: Zhang-sl
import unittest
from parking_4 import ParkingLot,SuperParkingBoy
class parking_4_test(unittest.TestCase):
    def test_park(self):
        super_parking_boy=SuperParkingBoy()
        super_parking_boy.get_car(['a','b','c','d','e','f'])
        super_parking_boy.get_plot([ParkingLot(5,2),ParkingLot(6,4),ParkingLot(8,8)])
        self.assertFalse(super_parking_boy.park())
if __name__ == '__main__':
    unittest.main()