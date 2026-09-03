 # Simple Inventory System — Dictionary mapping item names to quantities. Let user add stock, remove stock,
# and check if an item is low (below some threshold).

inventory = {}
threshold = 3

while True:
    user_input = input("Add, remove, check, or quit: ").strip().lower()
    # print(user_input)
   
    match user_input:
        case "add":
            print("\nAdding inventory...")
            item_name = input("Item: ").strip().title()
            item_qty = int(input("How many: "))
           
            if item_name in inventory:
                inventory[item_name] += item_qty
            else:
                inventory.setdefault(item_name, item_qty)
            print()
            continue

        case "remove":
            print("\nRemoving inventory...")
            item_name = input("Item: ").strip().title()
            item_qty = int(input("How many: "))
            if item_name in inventory:
                # if the amount to be removed is <= what we have in stock
                if item_qty <= inventory[item_name]:
                    inventory[item_name] -= item_qty
                    print(f"Removed {item_qty} of item {item_name}\n")
                else:
                    print("Not enough inventory to remove desired amount. Please try again... \n")
            else:
                print(f"Item {item_name} not found. Please try again. \n")
                continue
            print()
            continue

        case "check":
            print("\nChecking inventory...")
            c_inventory = inventory.copy()
            for item, qty in c_inventory.items():
                print(f"{item}: {qty}")
                if qty <= threshold:
                    print(f"The item '{item.lower()}' is getting low. Make sure to restock.\n")
                if qty == 0:
                    del inventory[item]
            print()
            continue

        case "quit":
            print("\nQuitting...")
            break



# issues:
# 1. user_input.lower() Doesn't Do Anything (done)
# 2. Repeated Item Name Normalization (done)
# 3. Inventory Can Contain Zero Quantity Items (done)

# ---------------- unfinished ----------------
# 4. No Validation for Quantity Input (i know, learning try/except error handling)
# 5. Negative Numbers Are Allowed when adding stock
# 6. setdefault() Isn't Really Needed
# 7. Empty Inventory Check
# 8. Coding duplication (learn functions)
# 9. Cleaner, more efficient low stock check.
# 10. More pythonic add operation using get().
