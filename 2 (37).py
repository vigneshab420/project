# 45. Reverse String - LeetCode
def reverse_string(s):
    return s[::-1]

# Test
strings = ["hello", "Python", "racecar", "a", ""]
for s in strings:
    print(f"Original: '{s}', Reversed: '{reverse_string(s)}'")