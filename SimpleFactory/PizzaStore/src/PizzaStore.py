
from Pizza import Pizza
from SimplePizzaFactory import SimplePizzaFactory

class PizzaStore:
    def __init__(self, pizzaFactory) -> None:
        self.pizzaFactory: SimplePizzaFactory = pizzaFactory

    def orderPizza(self, pizzaName: str) -> Pizza:
        pizza: Pizza = self.pizzaFactory.createPizza(pizzaName)
        
        pizza.prepare();
        pizza.bake();
        pizza.cut();
        pizza.box();

        return pizza

if __name__ == '__main__':
    pizzaStore = PizzaStore(SimplePizzaFactory())

    pizzaStore.orderPizza('cheese')
    pizzaStore.orderPizza('pizza')
    pizzaStore.orderPizza('pepperoni')
    pizzaStore.orderPizza('unkonw')