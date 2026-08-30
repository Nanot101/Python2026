# **Word Frequency Counter** — Take a paragraph of text, count how many times each word appears, store in a dictionary, print the top 3 most common words.


# the quick brown fox jumps over the lazy dog while the dog barks at the fox and the fox runs away the quick fox is clever but the lazy dog does not care the dog sleeps under the tree and the fox watches from the bushes the forest is quiet and the sun is warm the dog yawns and the fox smiles
word_dict ={}

text_input = str(input("Enter input: "))
words = text_input.split()

for word in words:
    word_dict[word] = word_dict.get(word, 0) + 1

# print(word_dict)

w_list = list(word_dict.items())
# print(w_list)
w_list.sort(key=lambda word: word[1], reverse=True)
print(w_list[:3])