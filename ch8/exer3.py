# 3. **Simple Calculator with Functions** — Write functions for `add`, `subtract`, `multiply`, `divide`, 
# then a main loop that asks the user for an operation and two numbers and calls the right function.

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def get_num():
    while True:
        try:
            num = int(input("Enter number: "))
        except ValueError:
            print("Please enter an integer.")
            continue
        else:
            return num


ops = ["add", "subtract", "multiply", "divide"]

x = get_num()
print("Now for the second number...\n")
y = get_num()

while True:
    operation = input("Enter operation: ").lower()
    if operation in ops:
        # print("Operation is in the list")
        match operation:
            case "add":
                print(add(x, y))
                break
            case "subtract":
                print(subtract(x, y))
                break
            case "multiply":
                print(multiply(x, y))
                break
            case "divide":
                print(divide(x, y))
                break
    else:
        print("Operation must be one of the following: 'add', 'subtract', 'multiply', 'divide'. Try again...")
        continue