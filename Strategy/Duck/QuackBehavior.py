
from abc import ABC, abstractmethod


class QuackBehavior(ABC):
    @abstractmethod
    def quack(self):
        pass


class Quack(QuackBehavior):
    def quack(self):
        print('Quack!')


class Squack(QuackBehavior):
    def quack(self):
        print('Chi!')


class MutaQuack(QuackBehavior):
    def quack(self):
        print('Do nothing.')

