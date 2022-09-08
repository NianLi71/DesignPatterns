from abc import ABC

# To deal with type hint, ref: 
# * https://adamj.eu/tech/2021/05/13/python-type-hints-how-to-fix-circular-imports/
# * https://stackoverflow.com/questions/39740632/python-type-hinting-without-cyclic-imports?noredirect=1&lq=1
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from GumballMachine import GumballMachine

class State(ABC):
    def __init__(self, gumballMachine: 'GumballMachine') -> None:
        self.gumballMachine = gumballMachine
    
    def insertQuarter(self):
        pass

    def ejectQuarter(self):
        pass

    def turnCrank(self):
        pass

    def dispense(self):
        pass

    def refill(self, count):
        # we can refill at any state
        self.gumballMachine.refillGumballs(count)

    def __str__(self) -> str:
        return f'*State: {self.__class__.__name__}'


class HasQuarter(State):
    def insertQuarter(self):
        print("You can't insert another quarter")

    def ejectQuarter(self):
        print('Quarter returned')
        self.gumballMachine.setState(self.gumballMachine.getNoQuarterState())

    def turnCrank(self):
        import random
        chance = random.random()
        if chance < 0.1 and self.gumballMachine.getGumballsCount() > 1:
            print('You are a winner!')
            self.gumballMachine.setState(self.gumballMachine.getWinnerState())
        else:
            print('You turned...')
            self.gumballMachine.setState(self.gumballMachine.getGumbalSoldState())


class NoQuarter(State):
    def insertQuarter(self):
        print('You inserted a quarter')
        self.gumballMachine.setState(self.gumballMachine.getHasQuarterState())

    def ejectQuarter(self):
        print("You haven't inserted a quarter")

    def turnCrank(self):
        print('You turned but there is no quarter')
        


class GumballSold(State):
    def dispense(self):
        self.gumballMachine.releaseBall()
        if self.gumballMachine.getGumballsCount() > 0:
            self.gumballMachine.setState(self.gumballMachine.getNoQuarterState())
        else:
            print('Oops, out of gumballs')
            self.gumballMachine.setState(self.gumballMachine.getOutOfGumballsState())


class OutOfGumballs(State):
    def insertQuarter(self):
        print("You can't insert a quarter, the machine is sold out")

    def turnCrank(self):
        print('You turned but there is no quarter')

    def refill(self, count):
        super().refill(count)
        self.gumballMachine.setState(self.gumballMachine.getNoQuarterState())


class WinnerState(State):
    def dispense(self):
        self.gumballMachine.releaseBall()
        self.gumballMachine.releaseBall()
        if self.gumballMachine.getGumballsCount() > 0:
            self.gumballMachine.setState(self.gumballMachine.getNoQuarterState())
        else:
            print('Oops, out of gumballs')
            self.gumballMachine.setState(self.gumballMachine.getOutOfGumballsState())