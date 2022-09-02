
from abc import ABC, abstractmethod
from FlyBehavior import FlyBehavior, FlyWithWings, FlyNoWay, FlyRocketPowered
from QuackBehavior import QuackBehavior, Quack, Squack


class Duck(ABC):
    def __init__(self, flyBehavior: FlyBehavior, quackBehavior: QuackBehavior) -> None:
        self.flyBehavior = flyBehavior
        self.quackBehavior = quackBehavior

    def swim(self):
        print('Swimming!')

    @abstractmethod
    def display(self):
        pass

    def performFly(self):
        self.flyBehavior.fly()

    def performQuack(self):
        self.quackBehavior.quack()


class MallardDuck(Duck):
    def __init__(self) -> None:
        super().__init__(flyBehavior=FlyWithWings(), quackBehavior=Quack())

    def display(self):
        print("I'm a real Mallard duck.")


class RubberDuck(Duck):
    def __init__(self) -> None:
        super().__init__(FlyNoWay(), Squack())

    def display(self):
        print("I'm a rubber duck!")


class ModelDuck(Duck):
    def __init__(self) -> None:
        super().__init__(FlyNoWay(), Quack())

    def display(self):
        print("I'm a model duck!")


def duckShowTime(duck: Duck):
    print('-'*10)
    print('A new duck show time!')
    duck.display()
    duck.performFly()
    duck.performQuack()
    duck.swim()

if __name__ == '__main__':
    duckShowTime(MallardDuck())
    
    duckShowTime(RubberDuck())

    duck = ModelDuck()
    duckShowTime(duck)
    duck.flyBehavior = FlyRocketPowered()
    duckShowTime(duck)