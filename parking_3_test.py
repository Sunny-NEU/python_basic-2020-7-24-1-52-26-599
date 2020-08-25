import unittest
from parking_3 import ParkingLot,SmartParkingBoy
class parking_3_test(unittest.TestCase):
    def test_park(self):
        smart_parking_boy=SmartParkingBoy()
        smart_parking_boy.get_car(['a','b','c','d','e','f'])
        smart_parking_boy.get_plot([ParkingLot(5,2),ParkingLot(6,4),ParkingLot(8,7)])
        smart_parking_boy.park()
        self.assertTrue(smart_parking_boy.plot_list[2].num_cur==8)
        # smart_parking_boy.get_plot([ParkingLot(5,2),ParkingLot(6,4),ParkingLot(8,8)])
        # smart_parking_boy.park()
        # self.assertTrue(smart_parking_boy.park())
if __name__ == '__main__':
    unittest.main()