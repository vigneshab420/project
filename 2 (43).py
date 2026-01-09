# 44. Power of Four - LeetCode
def is_power_of_four(n):
    if n <= 0:
        return False
    while n % 4 == 0:
        n //= 4
    return n == 1

# Test
numbers = [1, 4, 16, 64, 100, 256]
for num in numbers:
    print(f"{num} is power of four: {is_power_of_four(num)}")