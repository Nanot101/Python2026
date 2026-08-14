# **Shopping List with Total** — Let user add items with prices, store as a list of items, print the full list and running total.
# improve: format so that it only take floats in dollars. reformat list


user_input = ""
groceries = []
temp = []
total = 0.0


while True:
    user_input = str(input("Enter grocery item: "))
    if user_input != "q":
        temp.append(user_input)
    else:
        break

    user_input = str(input("Enter price of item: $"))
    if user_input != "q":
        user_input = float(user_input)
        temp.append(user_input)
        total += user_input
    else:
        break

    groceries.append(temp.copy())
    temp.clear()

for i in groceries:
    print(i)

print(f"Total: ${total}")