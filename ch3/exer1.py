#  **BMI Categorizer (extend project from section 2)** — Take the BMI number and print a category: underweight, normal, overweight, obese.

# height input
print("How tall are you? (Imperial)")
ft = int(input("Enter Feet: "))
inch = int(input("Enter Inches: "))

# height calc
total_in = ft * 12
total_in += inch
print(f"You are {total_in} inches tall")
cm = total_in * 2.54
print(f"You are {cm} cm tall")
meters = cm / 100
print(f"You are {meters} meters tall")



# weight input
print("How much do you weight? (Imperial)")
lbs = float(input("Enter weight in pounds (lbs): "))
# weight calc
kg = lbs/2.205
print(f"You weigh {kg:.2f} in kg")

#BMI calc
bmi = kg / (meters**2)
print(f"BMI: {bmi:.2f}")