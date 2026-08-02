# **Even/Odd & Divisibility Checker** — Ask for a number, print whether it's even/odd and whether it's divisible by 3, 5, and 15.

num = int(input("Enter number: "))
if (num % 2 == 0): 
    print("Even")
else:
    print("Odd")

if num % 3 == 0:
    print("Divisible by 3")

if num % 5 == 0:
    print("Divisible by 5")

if num % 15 == 0:
    print("Divisible by 15")
