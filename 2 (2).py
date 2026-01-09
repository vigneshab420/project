# 15. Nested Lists - HackerRank
students = []
for _ in range(int(input("Enter number of students: "))):
    name = input("Enter name: ")
    score = float(input("Enter score: "))
    students.append([name, score])

# Find second lowest score
scores = sorted(set([score for _, score in students]))
second_lowest = scores[1]

# Get names with second lowest score
names = sorted([name for name, score in students if score == second_lowest])
print("Students with second lowest score:")
for name in names:
    print(name)