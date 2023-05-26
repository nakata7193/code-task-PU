from restaurant.restaurant import Restaurant


def main():
    restaurant = Restaurant.get_instance()

    # Place orders
    restaurant.place_order("кралски", "чеснов")
    restaurant.place_order("класически", "кетчуп")
    restaurant.place_order("вегетариански", "чеснов") 