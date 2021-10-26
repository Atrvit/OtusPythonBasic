from abc import ABC
from homework_02.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):
    weight = 1000
    started = False
    fuel = 140
    fuel_consumption = 2

    def __init__(self, weight, fuel, fuel_consumption):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if not self.started:
            if self.fuel > 0:
                self.started = True
            else:
                raise LowFuelError('Нет топлива')

    def move(self, distance):
        if self.fuel - distance * self.fuel_consumption >= 0:
            self.fuel -= distance * self.fuel_consumption
        else:
            raise NotEnoughFuel('Недостаточно топлива для преодоления дистанции')
