# **FizzBuzz** — Classic: print numbers 1-100, but "Fizz" for multiples of 3, "Buzz" for multiples of 5, "FizzBuzz" for both.

max = 100

for i in range(1, max + 1, 1):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
