from restaurant.burger import BurgerFactory

class Kitchen:
    def prepare_burger(self, burger_type):
        burger = BurgerFactory.create_burger(burger_type)
        burger.prepare()
        return burger

class KitchenFactory:
    @staticmethod
    def create_kitchen():
        return Kitchen()


