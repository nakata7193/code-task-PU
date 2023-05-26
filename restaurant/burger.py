class Burger:
    def prepare(self):
        pass

    def serve(self):
        print("Бургерът е сервиран!")

class RoyalBurger(Burger):
    def prepare(self):
        print("Приготвяне на кралски бургер!")

class ClassicBurger(Burger):
    def prepare(self):
        print("Приготвяне на класически бургер!")

class VegetarianBurger(Burger):
    def prepare(self):
        print("Приготвяне на вегетариански бургер!")

class BurgerFactory:
    @staticmethod
    def create_burger(burger_type):
        if burger_type == "кралски":
            return RoyalBurger()
        elif burger_type == "класически":
            return ClassicBurger()
        elif burger_type == "вегетариански":
            return VegetarianBurger()
        else:
            raise ValueError("Невалиден вид бургер!")

class BurgerDecorator(Burger):
    def __init__(self, burger):
        self.burger = burger

    def prepare(self):
        self.burger.prepare()

    def serve(self):
        self.burger.serve()