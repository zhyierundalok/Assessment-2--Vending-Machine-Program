items = {
    'A1': {'Name': 'Lays Classic Chips', 'Price': 5.30},
    'A2': {'Name': 'Takis', 'Price': 4.75},
    'A3': {'Name': 'Sun Chips', 'Price': 6.78},
    'A4': {'Name': 'Pringles', 'Price': 5.93},
    'A5': {'Name': 'Bugles', 'Price': 3.55},
    'B1': {'Name': 'Coca Cola', 'Price': 2.25},
    'B2': {'Name': 'Fanta', 'Price': 3.00},
    'B3': {'Name': 'Sprite', 'Price': 2.75},
    'B4': {'Name': 'Pepsi', 'Price': 2.62},
    'B5': {'Name': 'Mountain Dew', 'Price': 1.98},
    'C1': {'Name': 'M&Ms', 'Price': 0.75},
    'C2': {'Name': 'Oreo', 'Price': 2.80},
    'C3': {'Name': 'Chupa Chups', 'Price': 0.50},
    'C4': {'Name': 'Haribo', 'Price': 2.18},
    'C5': {'Name': 'Kitkat', 'Price': 2.51}
}

print("Welcome to the Vending Machine!\n")
print("Available Items:")

for key, item in items.items():
    print(f"{key}: {item['Name']} - ${item['Price']:.2f}")

def vending_machine():
    while True:
        
        item_key = input("Enter the item code (e.g., A1): ").strip().upper()

        if item_key not in items:
            print("Selection Invalid. Please try again.\n")
            continue

        selected_item = items[item_key]
        print(f"\nYou selected {selected_item['Name']} which costs ${selected_item['Price']:.2f}.")

        try:
            money_input = float(input("Insert money: $"))
            if money_input <= 0:
                print("Invalid money input. Please try again.\n")
                continue
        except ValueError:
            print("Invalid input. Please enter a valid amount.\n")
            continue

        if money_input < selected_item['Price']:
            print("Insufficient money. Please try again and insert enough money.\n")
            continue

        print(f"\nDispensing {selected_item['Name']}...")
        print("Item Dispensed!")

        change = money_input - selected_item['Price']
        if change > 0:
            print(f"Your change is: ${change:.2f}")
        else:
            print("No change to return.")

        print("\nThank you for using the vending machine!")
        break
vending_machine()