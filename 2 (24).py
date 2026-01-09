# 42. Power of Two - LeetCode
def is_power_of_two(n):
    if n <= 0:
        return False
    return (n & (n - 1)) == 0

# Test
numbers = [1, 2, 3, 4, 5, 8, 16, 24, 32]
for num in numbers:
    print(f"{num} is power of two: {is_power_of_two(num)}")