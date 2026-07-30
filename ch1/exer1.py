# **Mad Libs Generator** — Ask the user for a noun, verb, adjective, and place via `input()`, plug them into a pre-written story template, print the result.

noun = "Noun"
verb = "Verb"
adj = "Adjective"

print(noun)
print(verb)
print(adj)

noun = str(input("Enter noun: "))
verb = str(input("Enter verb: "))
adj = str(input("Enter adjective: "))

print(noun)
print(verb)
print(adj)


print(f"The {adj} {noun} did that and {verb} over there.")