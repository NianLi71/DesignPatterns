
from Pizza import Pizza, CheesePizza, PepperoniPizza


class SimplePizzaFactory:
    def createPizza(self, type: str) -> Pizza:
        if (type == 'cheese'):
            return CheesePizza()
        elif (type == 'pepperoni'):
            return PepperoniPizza()
        elif type == 'pizza':
            return Pizza()
        else:
            raise Exception(f'Do not konw the type: "{type}" of Pizza to order.')