# Simple Inventory System — Dictionary mapping item names to quantities. Let user add stock, remove stock,
# and check if an item is low (below some threshold).

inventory = {}
threshold = 3

while True:
    user_input = input("Add, remove, check, or quit: ")
    user_input.lower()
    print(user_input)
   
    match user_input:
        case "add":
            print("\nAdding inventory...")
            item_name = input("Item: ")
            item_name = item_name.lower()
            item_name = item_name.capitalize()
            item_qty = int(input("How many: "))
            if item_name in inventory:
                inventory[item_name] += item_qty
            else:
                inventory.setdefault(item_name, item_qty)

            print()
            continue
        case "remove":
            print("\nRemoving inventory...")
            item_name = input("Item: ")
            item_name = item_name.lower()
            item_name = item_name.capitalize()
            item_qty = int(input("How many: "))
            if item_name in inventory:
                inventory[item_name] -= item_qty

                print(f"Removed {item_qty} of item {item_name}\n")
            else:
                print(f"Item {item_name} not found. Please try again. \n")
                continue
            print()
            continue
        case "check":
            print("\nChecking inventory...")
            for item, qty in inventory.items():
                print(f"{item}: {qty}")
                if qty <= threshold:
                    print(f"The item '{item.lower()}' is getting low. Make sure to restock.\n")
           
            print()
            continue
        case "quit":
            print("\nQuitting...")
            break