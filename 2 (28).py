# 16. Finding the Percentage - HackerRank
n = int(input("Enter number of students: "))
student_marks = {}

for _ in range(n):
    name, *marks = input("Enter name and marks: ").split()
    student_marks[name] = list(map(float, marks))

query_name = input("Enter student name to query: ")
marks = student_marks[query_name]
average = sum(marks) / len(marks)
print(f"{average:.2f}")