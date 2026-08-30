# 1. Basic Access.  Given student = {"name": "Maria", "grade": 89, "subject": "Math"}, print the student's name and grade using key access.

print("\nEx 1")
student = {"name": "Maria", "grade": 89, "subject": "Math"}
print(student["name"])
# print only the keys, values, items
print(student.keys())
print(student.values())
print(student.items())
# formatting
for key, value in student.items():
    print(f"{key}: {value}")
print()

# 2. Add and Update.    Start with car = {"brand": "Toyota", "year": 2020}. Add a new key "color" with value "red", then update "year" to 2023.

print("\nEx 2")
car = {"brand": "Toyota", "year": 2020}
car["color"] = "red"
print(car)
car["year"] = 2023
print(car)
print()


# 3. Safe Access with .get().   Given inventory = {"apples": 10, "bananas": 5}, use .get() 
# to print the count of "oranges" — but instead of None, it should print 0 if the key doesn't exist.

print("\nEx 3")
inventory = {"apples": 10, "bananas": 5}
print(inventory.get("oranges", 0))
print()


# 4. Delete a Key.  Given profile = {"username": "coder123", "email": "a@b.com", "temp_field": "delete_me"}, 
# remove "temp_field" from the dictionary. Do it two different ways (del and .pop()).

print("\nEx 4")
profile = {"username": "coder123", "email": "a@b.com", "temp_field": "delete_me"}
profile_copy = profile.copy()
del profile["temp_field"]
print(profile)

pp = profile_copy.pop("temp_field", "Missing")
print(pp)
print()


# 5. Loop and Print.    Given prices = {"coffee": 3.5, "tea": 2.5, "juice": 4.0}, loop through the dictionary and print each item like:
# coffee costs $3.5
# tea costs $2.5
# juice costs $4.0

print("\nEx 5")
prices = {"coffee": 3.5, "tea": 2.5, "juice": 4.0}
for key, value in prices.items():
    print(f"{key} costs ${value}")
print()


# 6. Sum the Values.    Given scores = {"Alex": 85, "Sam": 92, "Jordan": 78}, calculate and print the total of all scores using .values().

print("\nEx 6")
scores = {"Alex": 85, "Sam": 92, "Jordan": 78}
points = 0
for value in scores.values():
    points += value
print(points)
print()


# 7. Find a Key by Value.   Given capitals = {"France": "Paris", "Japan": "Tokyo", "Italy": "Rome"}, 
# write code that finds and prints which country has "Tokyo" as its capital (without hardcoding the answer — search for it).

print("\nEx 7")
capitals = {"France": "Paris", "Japan": "Tokyo", "Italy": "Rome"}
for key, value in capitals.items():
    if value == "Tokyo":
        print(key)
        break
print()


# 8. Build a Dictionary from Scratch.       You're given two lists. Combine them into a single dictionary {"Anna": 28, "Ben": 34, "Cara": 22} 
# using a loop (don't use zip() yet — practice manually with indices, then try it again with zip()).

print("\nEx 8")
names = ["Anna", "Ben", "Cara"]
ages = [28, 34, 22]
d = {}

for i, name in enumerate(names):
    d[name] = ages[i]
print(d)

dzip = dict(zip(names, ages))
print(dzip)
print()


# 9. Count Occurrences.     Given the string "apple banana apple cherry banana apple", split it into words and build a dictionary that 
# counts how many times each word appears — without using Counter, just .get() or plain key checks.

print("\nEx 9")
words = "apple banana apple cherry banana apple"
words = words.split()
d = {}
for w in words:
    d.setdefault(w, 0)
    d[w] += 1
print(d)
print()

# 10. Merge Two Dictionaries.   Merge them so that user_prefs values override defaults where they overlap, 
# and the rest of defaults stays intact. Try it with .update(), and separately with the | operator.

print("\nEx 10")
defaults = {"theme": "light", "font_size": 12, "notifications": True}
user_prefs = {"font_size": 16}
merge_update = defaults.copy()
merge_update.update(user_prefs)
print(merge_update)

merge_pipe = defaults|user_prefs
print(merge_pipe)
print()