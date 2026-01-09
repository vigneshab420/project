# 35. Palindrome Number - LeetCode
def is_palindrome(x):
    if x < 0:
        return False
    return str(x) == str(x)[::-1]

# Test
numbers = [121, -121, 10, 12321, 12345]
for num in numbers:
    print(f"{num} is palindrome: {is_palindrome(num)}")