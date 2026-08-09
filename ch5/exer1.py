# **Palindrome Checker** — Ask for a word or phrase, strip spaces/punctuation, check if it reads the same backward.

words = str(input("Enter word or phrase: "))

if words[:] == words[::-1]:
    print("Palindrome")
else:
    print("Not palindrome")