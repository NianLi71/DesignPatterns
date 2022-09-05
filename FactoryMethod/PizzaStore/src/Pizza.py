
class Pizza:
    def prepare(self):
        print('Prepare pizza')

    def bake(self):
        print('Bake pizza')

    def cut(self):
        print('Cut')

    def box(self):
        print('Put into box')


def NYPizzaTag(func):
    def newFunc(*args, **kwargs):
        print('NY pizza special:', end='')
        func(*args, **kwargs)
    return newFunc


class NYCheesePizza(Pizza):
    @NYPizzaTag
    def prepare(self):
        print('Prepare CheesePizza')

    @NYPizzaTag
    def bake(self):
        print('Special bake with cheese')


class NYPepperoniPizza(Pizza):
    @NYPizzaTag
    def cut(self):
        print('Fancy cut with PepperoniPizza')



def ChicagoPizzaTag(func):
    def newFunc(*args, **kwargs):
        print('Chicago pizza special:', end='')
        func(*args, **kwargs)
    return newFunc


class ChicagoCheesePizza(Pizza):
    @ChicagoPizzaTag
    def prepare(self):
        print('Prepare CheesePizza')

    @ChicagoPizzaTag
    def bake(self):
        print('Special bake with cheese')


class ChicagoPepperoniPizza(Pizza):
    @ChicagoPizzaTag
    def cut(self):
        print('Fancy cut with PepperoniPizza')

