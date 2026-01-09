# 43. Power of Three - LeetCode
def is_power_of_three(n):
    if n <= 0:
        return False
    while n % 3 == 0:
        n //= 3
    return n == 1

# Test
numbers = [1, 3, 9, 27, 45, 81, 100]
for num in numbers:
    print(f"{num} is power of three: {is_power_of_three(num)}")