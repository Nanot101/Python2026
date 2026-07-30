# **Simple Unit Converter** — Ask for a temperature in Celsius, convert to Fahrenheit and Kelvin, print all three nicely formatted.

cel = float(input("Enter Celsius: "))
# print(cel)

# F = 1.8C + 32
far = (1.8*cel) + 32
print("----------")
print(f"Fahrenheit: {far}")

# K = C + 273.15
kel = cel + 273.15
print("----------")
print(f"Kelvin: {kel}")
