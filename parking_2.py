#!/usr/bin/env python
# -*- coding: utf-8 -*-
# !@Time: 2020/8/12 18:08
# !@Author: Zhang-sl
class ParkingLot(object):
    car_curr = [] #停车场现有的车辆列表


class ParkingBoy(object):
    # 停车小弟属性初始化
    def __init__(self):
        self.car_list = None  # 停车小弟需要停的车辆列表
        self.plot_list = None  # 停车场列表

    def get_car(self, car_list):
        self.car_list = car_list

    def get_plot(self, num):
        self.plot_list=[0]*num
        for i in range(num):
            pl = ParkingLot()
            self.plot_list[i] = pl

    def park(self):
        for i in range(len(self.car_list)):
            if i <= len(self.plot_list):
                self.plot_list[i].car_curr.append(self.car_list[i])  # 如果停车场数目大于车辆数，则依次停放即可
            else:
                j = i % len(self.plot_list)  # 如果车辆数大于停车场数，则顺序停完之后，再重新按照停车场顺序停车，直到停完
                self.plot_list[j].car_curr.append(self.car_list[j])
        print('车辆已全部顺序停在多个停车场...')

    def take(self):
        for i in range(len(self.car_list)):
            if i > len(self.plot_list):
                j = i % len(self.plot_list)
                self.plot_list[j].car_curr.pop(0)  # 按照停车顺序取车
            else:
                self.plot_list[i].car_curr.pop(0)
        print('车辆已经按照停放顺序取出，先停放的车辆先取走...')
