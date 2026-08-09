# **FizzBuzz** — Classic: print numbers 1-100, but "Fizz" for multiples of 3, "Buzz" for multiples of 5, "FizzBuzz" for both.

for i in range(1, 21, 1):
    if i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
