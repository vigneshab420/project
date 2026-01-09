# 14. Find the Runner-Up Score - HackerRank
n = int(input("Enter number of scores: "))
scores = list(map(int, input("Enter scores: ").split()))
unique_scores = sorted(set(scores), reverse=True)
print(f"Runner-up score: {unique_scores[1]}")