# 48. Remove Duplicates - Set Method
def remove_duplicates_set(arr):
    return list(set(arr))

# Test
arr = [1, 2, 3, 3, 4, 4, 5, 5, 5]
print(f"Original: {arr}")
print(f"After removing duplicates (set): {remove_duplicates_set(arr)}")