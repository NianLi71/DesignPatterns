from abc import ABC, abstractmethod
from Pizza import *


class PizzaStore(ABC):
    def orderPizza(self, type: str) -> Pizza:
        pizza: Pizza = self._createPizza(type)
        
        pizza.prepare();
        pizza.bake();
        pizza.cut();
        pizza.box();

        return pizza

    @abstractmethod
    def _createPizza(self, type: str) -> Pizza:
        pass


class NYPizzaStore(PizzaStore):
    def _createPizza(self, type: str) -> Pizza:
        if (type == 'cheese'):
            return NYCheesePizza()
        elif (type == 'pepperoni'):
            return NYPepperoniPizza()
        elif type == 'pizza':
            return Pizza()
        else:
            raise Exception(f'Do not konw the type: "{type}" of Pizza to order.')


class ChicagoPizzaStore(PizzaStore):
    def _createPizza(self, type: str) -> Pizza:
        if (type == 'cheese'):
            return ChicagoCheesePizza()
        elif (type == 'pepperoni'):
            return ChicagoPepperoniPizza()
        elif type == 'pizza':
            return Pizza()
        else:
            raise Exception(f'Do not konw the type: "{type}" of Pizza to order.')


def clientOrderPizza(store: PizzaStore):
    store.orderPizza('cheese')      
    store.orderPizza('pepperoni')
    store.orderPizza('pizza')    


if __name__ == '__main__':
    clientOrderPizza(NYPizzaStore())  

    clientOrderPizza(ChicagoPizzaStore())   