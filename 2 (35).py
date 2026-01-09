# 36. Roman to Integer - LeetCode
def roman_to_int(s):
    roman = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    
    total = 0
    prev = 0
    
    for char in s[::-1]:
        curr = roman[char]
        if curr < prev:
            total -= curr
        else:
            total += curr
        prev = curr
    
    return total

# Test
romans = ["III", "IV", "IX", "LVIII", "MCMXCIV"]
for roman in romans:
    print(f"{roman} = {roman_to_int(roman)}")