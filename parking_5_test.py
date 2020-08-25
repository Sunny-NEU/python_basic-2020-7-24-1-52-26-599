#!/usr/bin/env python
# -*- coding: utf-8 -*-
#!@Time: 2020/8/25 15:34
#!@Author: Zhang-sl
import unittest
from parking_5 import ParkingLot,ParkingDirector
class parking_5_test(unittest.TestCase):
    def test_park(self):
        parking_director=ParkingDirector()
        parking_director.get_car(['a','b','c','d','e','f'])
        parking_director.get_plot([ParkingLot(5,2),ParkingLot(6,4),ParkingLot(8,7)])
        parking_director.park()
        self.assertTrue(parking_director.plot_list[2].num_cur==8)
        # smart_parking_boy.get_plot([ParkingLot(5,2),ParkingLot(6,4),ParkingLot(8,8)])
        # smart_parking_boy.park()
        # self.assertTrue(smart_parking_boy.park())
    def test_boy_park(self):
        carlist=['a','b','c','d','e','f']
        plot_list=[ParkingLot(5,2),ParkingLot(6,4),ParkingLot(8,7)]
        parking_director = ParkingDirector()
        parking_director.manager_boy(5)
        parking_director.one_boy_park(2,carlist,plot_list)
        self.assertFalse(parking_director.one_boy_park(2,carlist,plot_list))
if __name__ == '__main__':
    unittest.main()