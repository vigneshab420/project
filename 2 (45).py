# 27. Find Factors - PrepInsta
def find_factors(arr, n):
    return [i for i in arr if n % i == 0]

# Test
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Factors of 12 from list: {find_factors(numbers, 12)}")
print(f"Factors of 15 from list: {find_factors(numbers, 15)}")