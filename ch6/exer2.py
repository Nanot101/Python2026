# **Grade Average Calculator** — Let the user enter multiple test scores into a list (until they type "done"), then print the average, highest, and lowest.

user_input = ""
test_scores = 0.0
calc_list = []

while True:
    user_input = str(input("Enter test scores: "))
    if user_input != "done":
        test_scores = float(user_input)
        calc_list.append(test_scores)
        print(calc_list)
    else:
        break

# calculations after loop
calc_list.sort()
# print(calc_list)

print(f"Lowest: {calc_list[0]}")

# average
total = 0.0
for score in calc_list:
    total += score
average = total / len(calc_list)
print(f"Average: {average}")

print(f"Highest: {calc_list[-1]}")