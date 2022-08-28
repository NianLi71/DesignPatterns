
from abc import ABCMeta, abstractmethod


class FlyBehavior(metaclass=ABCMeta):
    @abstractmethod
    def fly(self):
        pass


class FlyWithWings(FlyBehavior):
    def fly(self):
        print('Fly with wings.')


class FlyNoWay(FlyBehavior):
    def fly(self):
        print('Do nothing, can not fly.')


class FlyRocketPowered(FlyBehavior):
    def fly(self):
        print("I'm flying with a rocket!")