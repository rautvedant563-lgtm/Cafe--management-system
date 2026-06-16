# Define menu
menu = {
    'Pizza': 40,
    'Pasta': 50,
    'Burger': 60,
    'Salad': 70,
    'Coffee': 80
}

# Greeting
print("Welcome to VSR Restaurant")
print("Pizza: Rs40\nPasta: Rs50\nBurger: Rs60\nSalad: Rs70\nCoffee: Rs80")

# Taking order
order_total = 0

item_1 = input("Enter name of item you want to order: ")

if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item {item_1} has been added to your order.")
else:
    print(f"Sorry, we don't have {item_1} in our menu.")

another_order = input("Do you want to add another item? (Yes/No): ")

if another_order.lower() == "yes":
    item_2 = input("Enter the name of second item: ")

    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Item {item_2} has been added to your order.")
    else:
        print(f"Ordered item {item_2} is not available in the menu.")

print(f"The total amount to pay is Rs{order_total}")