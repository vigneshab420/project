# 50. Remove Duplicates - Preserve Order
def remove_duplicates_ordered(arr):
    seen = set()
    result = []
    for num in arr:
        if num not in seen:
            seen.add(num)
            result.append(num)
    return result

# Test
arr = [1, 2, 3, 3, 4, 4, 5, 1, 2]
print(f"Original: {arr}")
print(f"After removing duplicates (ordered): {remove_duplicates_ordered(arr)}")