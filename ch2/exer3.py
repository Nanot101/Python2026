# **Simple Change Maker** — Ask for a dollar amount owed and amount paid, calculate change owed using `//` and `%` to break it into dollars/quarters/dimes/nickels/pennies.
import math

owed = float(input("You owe $"))
owed *= 100
print(f"Owed: {owed}")

paid = float(input("You paid $"))
paid *= 100
print(f"Paid: {paid}")


amount = paid - owed
print(f"Amount: {amount}")


dollars = amount // 100
print(f"Dollar(s): {dollars}")

cents = amount % 100
print(f"Cent(s): {cents}")

# coin conversion
quarters = cents // 25
print(f"{quarters:.0f} quarters")
# update cents after quarters
cents = cents - (25*quarters)
#print(cents)

dimes = cents // 10
print(f"{dimes:.0f} dimes")
cents -= 10*dimes
#print(cents)

nickels = cents // 5
print(f"{nickels:.0f} nickels")
cents -= 5*nickels
#print(cents)

pennies = cents // 1
print(f"{pennies:.0f} pennies")
cents -= 1*pennies
#print(cents)