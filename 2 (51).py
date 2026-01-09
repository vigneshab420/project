# 29. Product of Smallest Pair - PrepInsta
def product_smallest_pair(arr, sum_limit):
    if len(arr) < 2:
        return -1
    
    arr.sort()
    if arr[0] + arr[1] <= sum_limit:
        return arr[0] * arr[1]
    else:
        return 0

# Test
arr = [5, 2, 4, 3, 9, 7, 1]
sum_limit = 9
print(f"Array: {arr}")
print(f"Product of smallest pair with sum <= {sum_limit}: {product_smallest_pair(arr, sum_limit)}")