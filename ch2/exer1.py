# **BMI Calculator** — Take height and weight as input, compute BMI, print the numeric result

# BMI = weight (kg) / height (in meters)^2

# height: using imperial so feet and inches. 
# convert that to metric:
# calc height to inches -> cm -> meters
# ft * 12 = in
# in * 2.54 = cm
# cm / 100 = meters


# weight: using imperial so pounds (lbs)
# convert that to metric:
# lbs -> kg = lbs/2.205

print("How tall are you? (Imperial)")
ft = int(input("Enter Feet: "))
inch = int(input("Enter Inches: "))

# calc imperial height to metric
total_in = ft * 12
total_in += inch
print(f"You are {total_in} inches tall")
cm = total_in * 2.54
print(f"You are {cm} cm tall")
meters = cm / 100
print(f"You are {meters} meters tall")

