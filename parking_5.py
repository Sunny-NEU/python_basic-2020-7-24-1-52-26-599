#!/usr/bin/env python
# -*- coding: utf-8 -*-
#!@Time: 2020/8/24 20:43
#!@Author: Zhang-sl
from parking_3 import SmartParkingBoy

class ParkingLot(object):
    def __init__(self,num_all,num_cur):
        self.num_all=num_all #停车场一共有多少停车位
        self.num_cur=num_cur #停车场已经停的车辆数


class ParkingDirector(SmartParkingBoy):
    boy_list=[]
    def manager_boy(self,num):
        for i in range(num):
            self.boy_list.append(SmartParkingBoy())
    def one_boy_park(self,loc,carlist,plotlist):
        one_boy=self.boy_list[loc]
        one_boy.get_car(carlist)
        one_boy.get_plot(plotlist)
        one_boy.park()