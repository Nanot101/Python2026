# 1. Swap without a temp variable
# Write a function swap(a, b) that returns a and b swapped, using tuple unpacking (not a temporary variable). Then try it on x, y = swap(x, y).

# print("Exer 1:")
# def swap(a,b):
#     a , b = b, a
#     return a, b

# print(swap(5, 9))

# x, y = swap(8, 7)
# print(x)
# print(y)
# print("\n\n")


# 2. Multiple return values
# Write divide_and_remainder(a, b) that returns both the quotient and remainder as a tuple. Call it and unpack both values in one line.

# print("Exer 2:")
# def divide_and_remainder(a, b):
#     quotient = a // b
#     remainder = a % b
#     return quotient, remainder
# # calling AND unpacking variables in one line (cooooool)
# quotient, remainder = divide_and_remainder(4,2)
# print(quotient)
# print(remainder)
# print("\n\n")


# 3. Coordinates as dict keys
# You're building a simple grid-based game. Store which cells are "occupied" using a dict where keys are (row, col) tuples. 
# Write a function is_occupied(grid, row, col) that checks membership. 

# print("Exer 3:")
# grid = {
#     (1, 0): True,
#     (1, 4): True,
#     (2, 3): False,
#     (0, 2): True,
#     (2, 5): False
# }

# def is_occupied(grid, row, col):
#     g, r, c = grid, row, col
#     if (r, c) in g:
#         # print("Cell in grid")
#         if g[(r, c)] == True:
#             print("Cell is occupied")
#             return True
#         else:
#             print("Cell is NOT occupied")
#             return False
#     else:
#         print("Cell not in grid")
#         return None

# print(is_occupied(grid, 1, 0))
# print(is_occupied(grid, 2, 2))
# print(is_occupied(grid, 2, 5))
# print("\n\n")

# QUESTION: Why not use a list of [row, col] pairs instead?
# ANSWER: Storing occupied cells in a dict performs better than having them as list elements. 
# When looking up/searching for occupied cells, a dict's O(1) search beats a list's O(n) search


# 4. Unpacking with *
# Given a tuple of exam scores (88, 92, 79, 95, 60, 85), write one line using star-unpacking to grab 
# the first score, the last score, and "everything in between" as separate variables.

# print("Exer 4:")
# exam_scores = (88, 92, 79, 95, 60, 85)
# first, *middle, last = exam_scores
# print(first)
# print(middle)
# print(type(middle))
# print(last)
# print("\n\n")


