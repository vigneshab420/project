# 33. N-Base Notation - PrepInsta
def to_n_base(num, base):
    if num == 0:
        return "0"
    
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    
    is_negative = num < 0
    num = abs(num)
    
    while num > 0:
        result = digits[num % base] + result
        num //= base
    
    return "-" + result if is_negative else result

# Test
print(f"10 in binary: {to_n_base(10, 2)}")
print(f"255 in hexadecimal: {to_n_base(255, 16)}")
print(f"100 in octal: {to_n_base(100, 8)}")
print(f"1000 in base 20: {to_n_base(1000, 20)}")