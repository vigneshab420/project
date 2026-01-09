# 28. List Comprehension Factors - PrepInsta
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = int(input("Enter a number: "))
result = [i for i in arr if n % i == 0]
print(f"Numbers in list that divide {n}: {result}")