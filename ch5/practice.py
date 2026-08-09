# Exercise 1: Basic Indexing
# Given the string below, print the first character, the last character, and the character at index 3.

print("Exercise 1")
s = "Programming"
first_char = s[0]
last_char = s[-1]
char = s[3]
print(first_char, last_char, char)
print()



# Exercise 2: Slicing Practice
# Given the string below, use slicing to:
# Print just "Python"
# Print just "Rocks"
# Print the whole string reversed

print("Exercise 2")
s = "Python Rocks"
print(s[7:])
print(s[:6])
print(s[::-1])
print()



# Exercise 3: Case Conversion
# Given the string below, convert it to all uppercase, then all lowercase, and print both results.

print("Exercise 3")
s = "Hello World"
print(s.upper())
print(s.lower())
print()



# Exercise 4: Clean the Input
# Given the messy string below, strip the extra whitespace and print the cleaned result. Also print the length of the string before and after stripping.

print("Exercise 4")
s = "     messy data here     "
print(len(s))
stripped = s.strip()
print(stripped)
print(len(stripped))
print()



# Exercise 5: Split a Sentence
# Given the sentence below, split it into a list of words and print:
# The list itself
# The number of words
# Just the third word

print("Exercise 5")
s = "the quick brown fox jumps over the lazy dog"
print(s.split())

# word_count = 0
# for i in s.split():
#     word_count += 1
# print(f"Word count: {word_count}")
print(f"Word count: {len(s.split())}")

s_list = s.split()
print(s_list[2])
print()



# Exercise 6: Join a List
# Given the list below, join it into a single string separated by commas, then join it again separated by dashes.

print("Exercise 6")
words = ["apple", "banana", "cherry", "date"]
print(", ".join(words))
print("-".join(words))
print()



# Exercise 7: Find and Replace
# Given the string below:
# Use .find() to find the index of the word "fox"
# Use .replace() to replace "fox" with "cat"
# Print both results

print("Exercise 7")
s = "the quick brown fox jumps over the lazy dog"
print(s.find("fox"))
print(s.replace("fox", "cat"))
print()



# Exercise 8: Check the Ending
# Given the list of filenames below, manually check (one at a time, using .endswith()) which ones end with .txt and print True/False for each.

print("Exercise 8")
f1 = "notes.txt"
print(f1.endswith(".txt"))
f2 = "image.png"
print(f2.endswith(".txt"))
f3 = "summary.txt"
print(f3.endswith(".txt"))
print()



# Exercise 9: Username from Email
# Given the email below, use .find() and slicing together to extract just the username part (everything before the @).

print("Exercise 9")
email = "coolcoder99@example.com"
print(email[:email.find("@")])
print()



# Exercise 10: Mini Pipeline (Combine Everything)
# Given the messy string below:
# Strip the whitespace
# Convert to lowercase
# Split into a list of words
# Join the words back together using a - instead of spaces
# Print the result after each step so you can see the transformation happen.

print("Exercise 10")
s = "   Learning PYTHON Is Fun   "
s = s.strip()
print(s)
s = s.lower()
print(s)
s = s.split()
print(s)
s = "-".join(s)
print(s)
print()