#!/usr/bin/env python
# -*- coding: utf-8 -*-
#!@Time: 2020/8/24 15:58
#!@Author: Zhang-sl
import unittest
from parking_2 import ParkingLot,ParkingBoy
class parking_2_test(unittest.TestCase):
    def test_park(self):
        parking_boy=ParkingBoy()
        parking_boy.get_car(['a','b','c','d','e','f'])
        parking_boy.get_plot(6)
        parking_boy.park()
        parking_boy.take()
        for plot in parking_boy.plot_list:
            self.assertFalse(plot.car_curr)
if __name__ == '__main__':
    unittest.main()