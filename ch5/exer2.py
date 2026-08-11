# **Caesar Cipher (basic)** — Shift each letter of a message by a fixed number of positions in the alphabet to "encrypt" it.

abc = "abcdefghijklmnopqrstuvwxyz"

msg = str(input("Enter message: "))
num = int(input("Enter number: "))
growing_str = ""
coded = ""

for i in msg:
    if abc.find(i) != -1:
        coded = abc[(abc.find(i) + num) % 26 ]
        growing_str += coded
    else:
        growing_str += i
   
print(growing_str)