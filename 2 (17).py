# 30. Absolute Difference - PrepInsta
def count_absolute_difference(arr, num, diff):
    count = 0
    for i in arr:
        if abs(i - num) <= diff:
            count += 1
    return count

# Test
arr = [12, 71, 34, 15, 11]
num = 13
diff = 2
print(f"Array: {arr}")
print(f"Numbers within {diff} of {num}: {count_absolute_difference(arr, num, diff)}")