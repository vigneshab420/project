# 39. Single Number - LeetCode
def single_number(nums):
    result = 0
    for num in nums:
        result ^= num
    return result

# Test
arrays = [
    [2, 2, 1],
    [4, 1, 2, 1, 2],
    [1]
]

for arr in arrays:
    print(f"Array: {arr}")
    print(f"Single number: {single_number(arr)}")