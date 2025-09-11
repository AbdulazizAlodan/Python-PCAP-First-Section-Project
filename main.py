from restaurant.chef import add_dish, remove_dish, update_price, place_order, display_menu

def main():
    menu = {}
    add_dish(menu, "Pizza", 12.99)
    add_dish(menu, "Pasta", 9.99)
    add_dish(menu, "Salad", 6.99)
    display_menu(menu)
    print()
    place_order(menu, "Pizza")
    display_menu(menu)
    print()
    update_price(menu, "Pizza", 13.99)
    display_menu(menu)
    print()
    remove_dish(menu, "Salad")
    add_dish(menu, "Salad", 6.99)

if __name__ == "__main__":
    main()