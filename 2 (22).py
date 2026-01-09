# 18. No Idea! - HackerRank
n, m = map(int, input("Enter n and m: ").split())
arr = list(map(int, input("Enter array: ").split()))
A = set(map(int, input("Enter set A: ").split()))
B = set(map(int, input("Enter set B: ").split()))

happiness = 0
for num in arr:
    if num in A:
        happiness += 1
    if num in B:
        happiness -= 1

print(f"Happiness score: {happiness}")