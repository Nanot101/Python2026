# **Word Counter & Analyzer** — Take a sentence, print word count, character count (no spaces), and the longest word.

msg = str(input("Enter message: "))

# word count
word_count = len(msg.split())
print(f"Word count: {word_count}")

# character count
char_count = len("".join(msg.split()))
print(f"Character count: {char_count}")

# longest word
long_word = ""
msg_list = msg.split()
for i in msg_list:
    if len(i) > len(long_word):
        long_word = i
print(f"Longest word: {long_word}")
