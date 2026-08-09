# **Multiplication Table Generator** — Ask for a number, print its multiplication table from 1 to 12 using a `for` loop.

num = int(input("Enter a whole number: "))
for j in range(1, 13):
    print(f"{num} x {j} = {num * j}")