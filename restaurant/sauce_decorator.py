from .sauce_decorator import BurgerDecorator

class SauceDecorator(BurgerDecorator):
    def __init__(self, burger, sauce):
        super().__init__(burger)
        self.sauce = sauce

    def add_sauce(self):
        print(f"Добавяне на сос {self.sauce} към бургера!")