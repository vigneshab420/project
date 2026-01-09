# 51. List Comprehension Basic
# Create list with comprehension
lst = [i for i in range(1, 11)]
print(f"List from 1 to 10: {lst}")

# Squares
squares = [x**2 for x in range(1, 6)]
print(f"Squares from 1 to 5: {squares}")

# Even numbers
evens = [x for x in range(1, 11) if x % 2 == 0]
print(f"Even numbers from 1 to 10: {evens}")

# Matrix using nested comprehension
matrix = [[i*j for j in range(1, 4)] for i in range(1, 4)]
print(f"3x3 Multiplication matrix: {matrix}")