from Car import Car


class ParkingLot:
    def __init__(self, capacity):
        # todo: 构造停车场所需的字段
        self.capacity = capacity
        self.cars = []
        pass

    def park_car(self, car: Car):
        # todo: 实现停车功能，成功停车后返回一个不重复的物体（object/uuid/……）作为停车票
        pass

    def take_car(self, ticket):
        # todo: 实现通过车票取车的功能
        pass


if __name__ == "__main__":
    parking_lot = ParkingLot(1)
    car = Car()
    ticket = parking_lot.park_car(car)
    car = parking_lot.take_car(ticket)
