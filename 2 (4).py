# 49. Remove Duplicates - In-Place
def remove_duplicates_inplace(nums):
    if not nums:
        return 0
    
    i = 0
    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]
    
    return i + 1

# Test
arr = [1, 1, 2, 2, 3, 4, 4, 5]
print(f"Original: {arr}")
length = remove_duplicates_inplace(arr)
print(f"After removing duplicates: {arr[:length]}")
print(f"New length: {length}")