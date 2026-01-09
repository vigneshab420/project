# 26. Reverse Integer - PrepInsta
def reverse_integer(x):
    sign = -1 if x < 0 else 1
    x = abs(x)
    res = 0
    
    while x != 0:
        digit = x % 10
        res = res * 10 + digit
        x = x // 10
    
    res = res * sign
    
    # Check 32-bit range
    if -2**31 <= res <= 2**31 - 1:
        return res
    else:
        return 0

# Test
print(f"Reverse of 123: {reverse_integer(123)}")
print(f"Reverse of -456: {reverse_integer(-456)}")
print(f"Reverse of 1534236469: {reverse_integer(1534236469)}")