# 12. Write a Function - HackerRank
def is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

year = int(input("Enter year: "))
print(f"Is {year} leap year? {is_leap(year)}")