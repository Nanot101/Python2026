# **Grade Calculator** — Ask for a numeric score, print the letter grade (A/B/C/D/F) using elif chains.
# improve: add A+, A- , etc

# A = 90+   B = 80-89.99    C = 70-79.99    D = 60-69.99    F = <=59.99


grade = float(input('Enter the grade (~0.01): '))

# FIXME: 89.99999999999999 = A (broke it)
if grade >= 90:
    print("A")
elif 80 <= grade <= 89.99:
    print("B")
elif 70 <= grade <= 79.99:
    print("C")
elif 60 <= grade <= 69.99:
    print("D")
else:
    print("F")