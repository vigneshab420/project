# 46. Move Zeroes - LeetCode
def move_zeroes(nums):
    i = 0
    for j in range(len(nums)):
        if nums[j] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
    return nums

# Test
arrays = [
    [0, 1, 0, 3, 12],
    [0, 0, 1],
    [1, 2, 3, 0, 0]
]

for arr in arrays:
    print(f"Original: {arr}")
    print(f"After moving zeroes: {move_zeroes(arr.copy())}")