# 37. Fizz Buzz - LeetCode
def fizz_buzz(n):
    result = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return result

# Test
n = 15
print(f"FizzBuzz up to {n}:")
for item in fizz_buzz(n):
    print(item)