# 23. Min and Max (NumPy) - HackerRank
import numpy as np

n, m = map(int, input("Enter rows and columns: ").split())
arr = np.array([input("Enter row: ").split() for _ in range(n)], int)

min_values = np.min(arr, axis=1)
max_of_min = np.max(min_values)
print(f"Maximum of minimum values: {max_of_min}")