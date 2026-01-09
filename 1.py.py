# 40. Contains Duplicate - LeetCode
def contains_duplicate(nums):
    return len(nums) != len(set(nums))

# Test
arrays = [
    [1, 2, 3, 1],
    [1, 2, 3, 4],
    [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
]

for arr in arrays:
    print(f"Array: {arr}")
    print(f"Contains duplicate: {contains_duplicate(arr)}")