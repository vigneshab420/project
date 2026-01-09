# 47. Merge Sorted Lists
import heapq

def merge_sorted_lists(a, b):
    return list(heapq.merge(a, b))

# Test
list1 = [1, 3, 5, 7]
list2 = [2, 4, 6, 8]
print(f"List 1: {list1}")
print(f"List 2: {list2}")
print(f"Merged: {merge_sorted_lists(list1, list2)}")