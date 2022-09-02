
class Pizza:
    def prepare(self):
        print('Prepare pizza')

    def bake(self):
        print('Bake pizza')

    def cut(self):
        print('Cut')

    def box(self):
        print('Put into box')

class CheesePizza(Pizza):
    def prepare(self):
        print('Prepare CheesePizza')

    def bake(self):
        print('Special bake with cheese')

class PepperoniPizza(Pizza):
    def cut(self):
        print('Fancy cut with PepperoniPizza')