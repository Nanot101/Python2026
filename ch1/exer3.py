# **Tip Calculator** — Ask for bill amount, tip percentage, and number of people; print the tip amount and per-person total.

bill = float(input("Enter Bill: "))
tip = float(input("Enter Tip percentage: "))
ppl = int(input("How many people: "))

tipAmount = bill * (tip/100)
print(f"Tip amount is: ${tipAmount:.2f}")

totBill = bill + tipAmount
print(f"Your total bill + tip is: ${totBill:.2f}")

perPerson = totBill / ppl
print(f"How much should each person pay: ${perPerson:.2f}")

check = perPerson * ppl
print(f"Checking math: ${check:.2f}")
