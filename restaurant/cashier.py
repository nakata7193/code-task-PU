from .sauce_decorator import SauceDecorator


class CashierCommand:
    def __init__(self, kitchen, burger_type, sauce):
        self.kitchen = kitchen
        self.burger_type = burger_type
        self.sauce = sauce

    def execute(self):
        burger = self.kitchen.prepare_burger(self.burger_type)
        burger_with_sauce = SauceDecorator(burger, self.sauce)
        burger_with_sauce.add_sauce()
        burger_with_sauce.serve()