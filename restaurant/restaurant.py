from .cashier import CashierCommand
from .kitchen import KitchenFactory


class Restaurant:
    instance = None

    @staticmethod
    def get_instance():
        if Restaurant.instance is None:
            Restaurant.instance = Restaurant()
        return Restaurant.instance

    def __init__(self):
        self.kitchen = KitchenFactory.create_kitchen()

    def place_order(self, burger_type, sauce):
        cashier = CashierCommand(self.kitchen, burger_type, sauce)
        cashier.execute()


restaurant = Restaurant.get_instance()