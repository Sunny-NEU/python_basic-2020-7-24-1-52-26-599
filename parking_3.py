#!/usr/bin/env python
# -*- coding: utf-8 -*-
#!@Time: 2020/8/24 16:46
#!@Author: Zhang-sl
'''
需求：构造一个聪明的停车小弟（Smart Parking Boy），他能够将车停在空车位最多的那个停车场
'''
class ParkingLot(object):
    def __init__(self,num_all,num_cur):
        self.num_all=num_all #停车场一共有多少停车位
        self.num_cur=num_cur #停车场已经停的车辆数

class SmartParkingBoy(object):
    def __init__(self):
        self.car_list=[]#车辆列表
        self.plot_list=[]#停车场列表
        self.max_plot=ParkingLot(0,0) #最大的停车场
        self.max_plot_loc=None #最大停车场位置
    #获取车辆列表
    def get_car(self,carlist):
        self.car_list=carlist
    #获取停车场列表
    def get_plot(self,plotlist):
        self.plot_list=plotlist

    # 查找停车位最多的停车场
    def find_max_plot(self):
        for i in range(len(self.plot_list)):
            if (self.plot_list[i].num_all-self.plot_list[i].num_cur)>=(self.max_plot.num_all-self.max_plot.num_cur):
                self.max_plot=self.plot_list[i]
                self.max_plot_loc=i
    #停车
    def park(self):
        for i in range(len(self.car_list)):#将每一辆车都停在停车位最多的停车场
            self.find_max_plot() #查找空车位最多的停车场
            if  not (self.max_plot.num_all-self.max_plot.num_cur):
                print('没有停车位了，无法继续停车')
                return 1
            self.max_plot.num_cur+=1
            self.plot_list[self.max_plot_loc]=self.max_plot #停完后，更新停车场列表，下次查再找空车位最大的停车场
