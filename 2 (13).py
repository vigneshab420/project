# 34. Two Sum - LeetCode
def two_sum(nums, target):
    num_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
    return []

# Test
nums = [2, 7, 11, 15]
target = 9
print(f"Two Sum: nums={nums}, target={target}")
print(f"Indices: {two_sum(nums, target)}")