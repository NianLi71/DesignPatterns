from States import *

debug = False

class GumballMachine:
    
    def __init__(self, count: int) -> None:
        self.hasQuarter = HasQuarter(self)
        self.noQuarter = NoQuarter(self)
        self.gumballSold = GumballSold(self)
        self.outOfGumballs = OutOfGumballs(self)
        self.winnerState = WinnerState(self)

        self.gumballs = count
        self.state = self.noQuarter

    def insertQuarter(self):
        self.state.insertQuarter()

    def ejectQuarter(self):
        self.state.ejectQuarter()

    def turnCrank(self):
        self.state.turnCrank()
        self.state.dispense()

    def refill(self, count):
        self.state.refill(count)
    
    def setState(self, state: State):
        self.state = state
        if debug:
            print(self.state)

    def refillGumballs(self, count):
        if count > 0:
            self.gumballs += count

    def getGumballsCount(self):
        return self.gumballs

    def getNoQuarterState(self) -> State:
        return self.noQuarter

    def getHasQuarterState(self) -> State:
        return self.hasQuarter

    def getGumbalSoldState(self) -> State:
        return self.gumballSold

    def getOutOfGumballsState(self) -> State:
        return self.outOfGumballs

    def getWinnerState(self) -> State:
        return self.winnerState

    def releaseBall(self):
        print('A gumball comes rolling out the slot')
        if self.gumballs > 0:
            self.gumballs -= 1

    def __str__(self) -> str:
        return f"\nGumball machine has {self.gumballs} inventory.\n"


if __name__ == '__main__':
    '''
    Consider changing test code into unittest
    '''
    gumballMachine = GumballMachine(10)
    print(gumballMachine)

    gumballMachine.insertQuarter()
    gumballMachine.turnCrank()
    print(gumballMachine)

    gumballMachine.insertQuarter()
    gumballMachine.ejectQuarter()
    gumballMachine.turnCrank()
    print(gumballMachine)

    gumballMachine.insertQuarter()
    gumballMachine.turnCrank()
    gumballMachine.insertQuarter()
    gumballMachine.turnCrank()
    gumballMachine.ejectQuarter()
    print(gumballMachine)

    gumballMachine.insertQuarter()
    gumballMachine.insertQuarter()
    gumballMachine.turnCrank()
    gumballMachine.insertQuarter()
    gumballMachine.turnCrank()
    gumballMachine.insertQuarter()
    gumballMachine.turnCrank()
    print(gumballMachine)

    gumballMachine.refill(10)
    print(gumballMachine)